import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import uuid

spec = importlib.util.spec_from_file_location('app', Path(__file__).resolve().parents[1] / 'server/app.py')
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)

class Contacts(unittest.TestCase):
    def payload(self, **extra):
        return dict(type='contact', name='Test buyer', email='test@example.invalid', **extra)

    def test_attribution_needs_separate_explicit_consent(self):
        for raw in [None, {}, {'consent': 'yes'}, {'consent': False}]:
            self.assertIsNone(app.parse_contact(self.payload(attribution=raw))['attribution'])

    def test_attribution_drops_pii_and_arbitrary_sources(self):
        raw = {'consent': True, 'first_source': 'chatgpt', 'last_source': 'test@example.invalid',
               'landing_path': '/kontakt/?email=private@example.invalid', 'language': 'en', 'prompt': 'private'}
        self.assertEqual(app.parse_attribution(raw), {'consent': True, 'first_source': 'chatgpt',
                         'last_source': 'unknown', 'language': 'en'})
        self.assertEqual(app.parse_attribution(dict(raw, landing_path='/en/vanilla-pudding/'))['landing_path'], '/en/vanilla-pudding/')
        for value in [[], {}, None]:
            app.parse_attribution(dict(raw, first_source=value, language=value))

    def test_same_submission_saved_and_notified_once(self):
        nonce = str(uuid.uuid4())
        with tempfile.TemporaryDirectory() as d, patch.object(app, 'LOCAL_DIR', Path(d)), \
             patch.object(app, 'IS_CLOUD_RUN', False), patch.object(app, 'send_zapier', return_value=True) as send:
            ids = []
            for _ in range(2):
                payload = app.parse_contact(self.payload())
                app.identify_submission(payload, nonce)
                ids.append(payload['submission_id'])
                app.deliver_contact(payload)
            self.assertEqual(ids[0], ids[1])
            self.assertRegex(ids[0], r'^lead_[a-f0-9]{32}$')
            self.assertEqual(send.call_count, 1)
            stored = list(Path(d).glob('contacts_*'))
            self.assertEqual(len(stored), 1)
            self.assertEqual(json.loads(stored[0].read_text())['submission_id'], ids[0])
            changed = app.parse_contact(self.payload(message='Different order'))
            app.identify_submission(changed, nonce)
            self.assertNotEqual(changed['submission_id'], ids[0])

    def test_storage_failure_cannot_be_a_successful_lead(self):
        payload = app.parse_contact(self.payload())
        app.identify_submission(payload, str(uuid.uuid4()))
        with patch.object(app, 'save_contact', side_effect=OSError('failed')), patch.object(app, 'send_zapier') as send:
            with self.assertRaises(OSError): app.deliver_contact(payload)
            send.assert_not_called()

    def test_cloud_conflict_does_not_resend(self):
        payload = app.parse_contact(self.payload())
        app.identify_submission(payload, str(uuid.uuid4()))
        with patch.object(app, 'IS_CLOUD_RUN', True), patch.object(app, 'gcs_put', return_value=False), patch.object(app, 'send_zapier') as send:
            self.assertEqual(app.deliver_contact(payload), 'stored_existing')
            send.assert_not_called()

    def test_newsletter_is_not_a_lead_and_has_no_attribution(self):
        payload = app.parse_contact(dict(type='newsletter', email='test@example.invalid', consent='yes',
                                   attribution={'consent': True, 'first_source': 'chatgpt'}))
        app.identify_submission(payload, str(uuid.uuid4()))
        self.assertTrue(payload['submission_id'].startswith('newsletter_'))
        self.assertNotIn('attribution', payload)


class HandlerContract(unittest.TestCase):
    def test_http_acceptance_failure_newsletter_and_preview(self):
        import threading
        import urllib.request
        import urllib.error
        from http.server import ThreadingHTTPServer
        with tempfile.TemporaryDirectory() as d, patch.object(app, 'LOCAL_DIR', Path(d)), \
             patch.object(app, 'IS_CLOUD_RUN', False), patch.object(app, 'send_zapier', return_value=True) as send, \
             patch.dict(app.os.environ, {'PREVIEW_READ_ONLY': '0'}):
            server = ThreadingHTTPServer(('127.0.0.1', 0), app.Handler)
            thread = threading.Thread(target=server.serve_forever, daemon=True); thread.start()
            app._rate.clear()
            def post(body):
                req = urllib.request.Request(f'http://127.0.0.1:{server.server_port}/api/contact',
                      data=json.dumps(body).encode(), headers={'Content-Type': 'application/json'})
                try:
                    with urllib.request.urlopen(req) as response: return response.status, json.load(response)
                except urllib.error.HTTPError as response: return response.code, json.load(response)
            try:
                raw = dict(type='contact', name='Test', email='test@example.invalid', requestId=str(uuid.uuid4()))
                code, result = post(raw)
                self.assertEqual(code, 200); self.assertRegex(result['lead_id'], '^lead_')
                self.assertEqual(post(raw)[1]['lead_id'], result['lead_id'])
                self.assertEqual(send.call_count, 1)
                self.assertNotIn('lead_id', post(dict(raw, honeypot='bot'))[1])
                self.assertNotIn('lead_id', post(dict(type='newsletter', email='test@example.invalid', consent='yes'))[1])
                with patch.object(app, 'save_contact', side_effect=OSError('simulated storage outage')):
                    code, result = post(dict(raw, requestId=str(uuid.uuid4())))
                    self.assertEqual(code, 502); self.assertNotIn('lead_id', result)
                with patch.dict(app.os.environ, {'PREVIEW_READ_ONLY': '1'}):
                    self.assertEqual(post(raw)[0], 403)
            finally:
                server.shutdown(); server.server_close(); thread.join()

if __name__ == '__main__': unittest.main()
