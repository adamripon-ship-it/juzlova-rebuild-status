import sys
from pathlib import Path
import unittest
from decimal import Decimal
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from report_orders import summarize

class Orders(unittest.TestCase):
    def row(self, **kw):
        return dict(dict(order_id='1', status='paid', currency='CZK', revenue_basis='excluding_vat',
                         order_value='100', refund_value='0', observed_ai_source='chatgpt'), **kw)
    def test_quotes_not_revenue_and_refunds_subtracted(self):
        result = summarize([self.row(), self.row(order_id='2', status='quoted'),
                            self.row(order_id='3', status='partially_refunded', refund_value='25')])
        self.assertEqual(result[0]['orders'], 2)
        self.assertEqual(result[0]['net_revenue_czk'], Decimal('175'))
    def test_duplicates_and_mixed_currency_rejected(self):
        for rows in [[self.row(), self.row()], [self.row(currency='EUR')], [self.row(order_value='NaN')]]:
            with self.assertRaises(ValueError): summarize(rows)
    def test_self_reported_separate_from_observed(self):
        result = summarize([self.row(observed_ai_source='', self_reported_ai_source='perplexity')])
        self.assertEqual(result[0]['attribution_method'], 'self_reported')
if __name__ == '__main__': unittest.main()
