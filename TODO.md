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
- [ ] **Resubmit the sitemap in Google Search Console.** Sitemaps → submit
      `https://www.juzlova.cz/sitemap.xml`. Open since the address change on
      16 September 2026.
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

- [ ] **Product labels: finish
      [#27](https://github.com/adamripon-ship-it/juzlova-rebuild-status/pull/27).**
      Rebuild it on today's `main` rather than merging the old branch (it is
      far behind). Add ingredients, allergens, nutrition per 100 g, storage
      and preparation to the two dumpling-mix pages, in all four languages,
      from the label transcription in that PR. Link the Facebook and Firmy.cz
      review profiles. Do not invent any rating. Then close #27.
      - Blocked on the owner for: label photos of the **pudding, cocoa and
        vanilla sugar**, the **Firmy.cz score**, and the three label
        questions at the end of `docs/PRODUCT-LABELS.md` on the #27 branch.
- [ ] **Pudding packs and enquiry source: redo the useful parts of
      [#28](https://github.com/adamripon-ship-it/juzlova-rebuild-status/pull/28).**
      That branch conflicts in 198 files, so rebuild on today's `main` and do
      not merge it. Two parts are worth keeping:
      1. The pudding's product data (JSON-LD) lists both packs: **1 kg / 60 Kč
         and 400 g / 30 Kč**.
      2. The contact form records which channel an enquiry came from, only
         with the visitor's consent. Phone or e-mail clicks are not counted
         as sales.

      Then close #28 with a comment linking the new PR.

## 💡 Ideas, not scheduled

- [ ] Anything new for the site (copy, recipes, photos, design): add it here
      with a date and who asked.

---

## ✅ Done

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
