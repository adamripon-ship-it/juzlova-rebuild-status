# Pending product images (Higgsfield, approved by the owner 2026-09-23)

Needs network access to `d8j0ntlcm91z4.cloudfront.net` and
`d2ol7oe51mr4n9.cloudfront.net` (environment: Custom network access).

## Paper-bag hero photos (replace the current product images)

Resize to 1200 px wide WebP plus a 640 px variant, keep the file names.

| Product | Target file | Source |
|---|---|---|
| Kakao 500 g | img/produkt-kakao.webp | https://d8j0ntlcm91z4.cloudfront.net/user_3Bj5jSbouMgBXvv0eqo1wQl5cMI/hf_20260923_231235_510af7a5-176a-495b-8064-e2612f1bf5fe.png |
| Bramborové knedlíky 5 kg | img/produkt-bramborove-knedliky.webp | https://d8j0ntlcm91z4.cloudfront.net/user_3Bj5jSbouMgBXvv0eqo1wQl5cMI/hf_20260923_231344_10dee798-b301-4020-98c8-565f0d878d4c.png |
| Chlupaté knedlíky 5 kg | img/produkt-chlupate-knedliky.webp | https://d8j0ntlcm91z4.cloudfront.net/user_3Bj5jSbouMgBXvv0eqo1wQl5cMI/hf_20260923_231344_80658e41-6e7c-4879-8ff1-caeb41d41e45.png |
| Vanilkový puding 1 kg | img/produkt-vanilkovy-puding.webp | https://d8j0ntlcm91z4.cloudfront.net/user_3Bj5jSbouMgBXvv0eqo1wQl5cMI/hf_20260923_231344_fcdb073f-6fc2-43ad-9c51-f00b49f591f4.png |
| Vanilínový cukr 1 kg | img/vanilkovy-cukr-kilo.webp | https://d8j0ntlcm91z4.cloudfront.net/user_3Bj5jSbouMgBXvv0eqo1wQl5cMI/hf_20260923_231344_f5c2d51b-675f-4098-94db-b0abb9670f71.png |

## Real packaging photos (owner's real labels composited back in)

Rendered by `pack_html()` in build_site.py once the file exists.

| Product | Target file | Source |
|---|---|---|
| Vanilkový puding 400 g + 1 kg | img/baleni-vanilkovy_pudink.webp | https://d2ol7oe51mr4n9.cloudfront.net/user_3Bj5jSbouMgBXvv0eqo1wQl5cMI/7364f5eb-6186-414f-a0c0-559d5bc66378.png |
| Kakao 500 g | img/baleni-kakao_holandskeho_typu.webp | https://d2ol7oe51mr4n9.cloudfront.net/user_3Bj5jSbouMgBXvv0eqo1wQl5cMI/0571c8e5-299a-4e05-8b34-b465d63d2d8b.png |

Still missing: real packaging photos for the dumpling mixes and sugar.
After adding: bump ASSET_VER, run build_site.py and verify_refs.py, check
product pages on phone and desktop, then open a PR.
