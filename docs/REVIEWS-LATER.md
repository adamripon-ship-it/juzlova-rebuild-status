# Customer reviews — Google + Seznam

The site shows star ratings from:

- **Google Maps** — listing “Juzlova - Potravinářské směsi”
- **Seznam Firmy.cz** — firm id 12906730

Build refreshes Seznam from the Mapy suggest API (`reviewPercentage`).
Google uses Places API when `GOOGLE_PLACES_API_KEY` + `GOOGLE_PLACE_ID` are set;
otherwise the last known public scan is shown and still linked to the live Maps profile.

Do not invent stars. Cached Google figures must be replaced once Places API (or a fresh verified scan) is available.
