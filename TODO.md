# To-do list — juzlova.cz

**Every AI agent and developer reads this before doing anything.** It is the
current plan. Check what is open, don't redo what is done, and update this
file in the same pull request that finishes or changes an item.

Scheduled for the week of **2 November 2026**.

How to use it:

- Tick an item (`- [x]`) and add the PR link when it is done. Don't delete it.
- Add new items under the right heading, with a date and who asked.
- Items marked **👤 owner** need a person with the right login. An AI agent
  must not try to do them, and should remind the person instead.
- Everything still follows [`AGENTS.md`](AGENTS.md). The handbook is
  [`docs/website/`](docs/website/README.md).

---

## 👤 Owner tasks (need your accounts)

- [ ] **Protect `main` on GitHub.** Settings → Branches → add a rule for
      `main`: require a pull request, and require the "Build check" status
      check to pass. Merging to `main` publishes the live site within about
      2 minutes.
- [ ] **Add the developers on GitHub.** Settings → Collaborators, with
      **Write** access. Send them `docs/website/README.md` to start.
- [ ] **Delete the unused Cloud Run service** `juzlova-web` in
      **europe-west3**, in the Google Cloud console (project `aiapply-ch`).
      Only once you're sure nothing uses it. ⚠️ Do **not** touch the
      europe-west4 service: that is the live site.
- [ ] **Renew the domain `juzlova.cz` at ACTIVE 24 before 20 October 2027.**
      Put a reminder in the calendar now.
- [ ] *(Optional)* **Turn on Google Analytics.** Create a GA4 property and
      put its `G-…` ID in the Cloud Run setting
      `GOOGLE_ANALYTICS_MEASUREMENT_ID`. See
      [`docs/GA4-AEO.md`](docs/GA4-AEO.md).
- [ ] **Check contact-form e-mail after the 2026-10-30 changes.** Send one
      enquiry with the new delivery option and confirm it reaches the client
      (2026-10-30, Adam).

## 🛠️ Development work (an AI agent or developer can do these)

- [ ] **Product labels: remaining data.** Dumpling-mix label data is published.
      - **👤 owner:** confirm the E 223 sulphite level with the dried-potato
        supplier, then publish the potato mix allergen line.
      - **👤 owner:** send label photos of the **pudding, cocoa and vanilla
        sugar**, and the **Firmy.cz score**.

- [ ] **Euro amounts on EN and DE pages.** Approximate, at the CNB rate of
      30 October 2026 (`EUR_CZK` in `build_site.py`, named in `eur_note`).
      Review each quarter with the prices (2026-10-31, Adam).
- [ ] **Native-speaker check of German and Slovak copy** before larger copy
      changes, including the German product names (2026-10-31, Adam).

## 💡 Ideas, not scheduled

- [ ] Anything new for the site (copy, recipes, photos, design): add it here
      with a date and who asked.

---

## ✅ Done

- [x] 2026-10-31: pudding product data lists both packs, and the contact form records the visitor's channel only with analytics consent (dormant until GA is on). Replaces #28 (Adam).
- [x] 2026-10-31: sitemap resubmitted in Google Search Console (Adam).
- [x] 2026-10-31: hero button contrast raised to about 8:1 and phone numbers kept on one line, after a 116-page iOS Simulator audit (Adam).
- [x] 2026-10-30: owner's PDF content corrections, posting removal, translation
      review and responsive fixes
      ([#48](https://github.com/adamripon-ship-it/juzlova-rebuild-status/pull/48)).
      Humpolec pick-up stays. The en/de/sk wording has had an AI review, not a
      native one.
- [x] 2026-10-29: live site checked byte-for-byte against `main`; they match.
- [x] 2026-10-29: website handbook in `docs/website/`, with the site map, all
      page copy and the image gallery generated automatically
      ([#46](https://github.com/adamripon-ship-it/juzlova-rebuild-status/pull/46)).
- [x] 2026-10-29: `develop` branch created as the shared work branch.
- [x] 2026-10-29: star ratings fixed on the větrníčky recipe
      ([#43](https://github.com/adamripon-ship-it/juzlova-rebuild-status/pull/43)).
- [x] 2026-10-29: closed stale PRs
      [#19](https://github.com/adamripon-ship-it/juzlova-rebuild-status/pull/19)
      and [#20](https://github.com/adamripon-ship-it/juzlova-rebuild-status/pull/20).
