# 7. Making changes

[← Back to the handbook](README.md)

Everything happens on GitHub. You do **not** need access to Google Cloud or
Cloudflare to change the website.

---

## Branches

| Branch | Purpose |
|---|---|
| `main` | **The live website.** Every merge here is published within about 2 minutes |
| `develop` | Shared work branch, a copy of `main`. Start new work here |

## Step by step

1. **Get the code**
   ```sh
   git clone https://github.com/adamripon-ship-it/juzlova-rebuild-status.git
   cd juzlova-rebuild-status
   git checkout develop
   git checkout -b my-change          # your own branch
   ```

2. **Edit the source**, never the generated HTML. See
   [where the words come from](04-editorial.md#where-the-words-come-from).
   Styling is in `assets/site.css`. Layout and SEO are in `scripts/build_site.py`.

3. **Rebuild and check**
   ```sh
   python3 scripts/build_site.py      # regenerate every page
   python3 scripts/export_docs.py     # refresh this handbook's site map and copy
   python3 scripts/verify_refs.py     # confirm no broken links
   ```

4. **Look at it in a browser**
   ```sh
   scripts/dev_server.sh              # then open http://localhost:8080
   ```
   (Needs nginx installed. Some bugs only show on screen, not in the code.)

5. **Commit everything**, the source and the regenerated files together, and
   open a pull request on GitHub.

6. **Wait for the green tick.** The "Build check" rebuilds the whole site and
   fails if anything you committed is out of date or a link is broken.

7. **Merge.** Merging into `develop` collects work. Merging into `main`
   publishes it. Then check the live page.

## Checklist before merging to `main`

- [ ] Changed the same text in all four languages (if it was a copy change)
- [ ] Followed the [house rules](04-editorial.md#house-rules-for-writing)
- [ ] Bumped `ASSET_VER` in `build_site.py` if `site.css` or `site.js` changed
- [ ] Ran `optimize_images.py` if you added images
- [ ] Viewed the page in a browser, on desktop and phone width
- [ ] "Build check" is green

## Ask the owner first

- Any DNS change
- Deleting a Cloud Run service or storage bucket
- Force-pushing `main`
- Anything that changes what visitors see without an easy way back

Full developer rules: [`AGENTS.md`](../../AGENTS.md).
