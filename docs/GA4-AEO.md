# Google Analytics for this site

The cookie bar stays hidden until a real Google Analytics ID exists.
Nobody invents a `G-` number.

When you have the ID from Google Analytics (it looks like `G-XXXX`):

1. Put it in the Cloud Run setting `GOOGLE_ANALYTICS_MEASUREMENT_ID`.
2. Rebuild or redeploy. The cookie bar then appears.
3. After a visitor accepts cookies, the site can also mark visits that came from ChatGPT, Perplexity, Claude, Gemini, or Copilot as `ai_referral`.

Until that ID is in place, no Google tracking script loads.
