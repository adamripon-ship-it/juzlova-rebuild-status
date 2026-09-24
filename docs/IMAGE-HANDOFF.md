# Pending product images (Higgsfield, approved by the owner 2026-09-23)

Needs network access to `d8j0ntlcm91z4.cloudfront.net` and
`d2ol7oe51mr4n9.cloudfront.net` (environment: Custom network access).

## Paper-bag hero photos with ingredients (replace the current product images)

Styled 2026-09-24: cacao pods and beans; dug potatoes with flowers; raw potatoes
with grated potato; vanilla pods, orchid flowers and vine.

Resize to 1200 px wide WebP plus a 640 px variant, keep the file names.

| Product | Target file | Source |
|---|---|---|
| Kakao 500 g | img/produkt-kakao.webp | https://d8j0ntlcm91z4.cloudfront.net/user_3Bj5jSbouMgBXvv0eqo1wQl5cMI/hf_20260924_101533_21e04cbc-b60a-4148-abd2-a206e7e167f5.png |
| Bramborové knedlíky 5 kg | img/produkt-bramborove-knedliky.webp | https://d8j0ntlcm91z4.cloudfront.net/user_3Bj5jSbouMgBXvv0eqo1wQl5cMI/hf_20260924_101533_9dfad708-9a1e-4133-a685-f7524d8163ba.png |
| Chlupaté knedlíky 5 kg | img/produkt-chlupate-knedliky.webp | https://d8j0ntlcm91z4.cloudfront.net/user_3Bj5jSbouMgBXvv0eqo1wQl5cMI/hf_20260924_101533_b8d5dae2-2c4c-4132-a783-adb34ff1fd83.png |
| Vanilkový puding 1 kg | img/produkt-vanilkovy-puding.webp | https://d8j0ntlcm91z4.cloudfront.net/user_3Bj5jSbouMgBXvv0eqo1wQl5cMI/hf_20260924_101534_66679af7-41d4-49e4-8729-9a7797236044.png |
| Vanilínový cukr 1 kg | img/vanilkovy-cukr-kilo.webp | https://d8j0ntlcm91z4.cloudfront.net/user_3Bj5jSbouMgBXvv0eqo1wQl5cMI/hf_20260924_101533_6b7aff12-45b5-4f43-ac66-3b593f4f75b3.png |

## Real packaging photos (owner's real labels composited back in)

Rendered by `pack_html()` in build_site.py once the file exists.

| Product | Target file | Source |
|---|---|---|
| Vanilkový puding 400 g + 1 kg | img/baleni-vanilkovy_pudink.webp | https://d2ol7oe51mr4n9.cloudfront.net/user_3Bj5jSbouMgBXvv0eqo1wQl5cMI/7364f5eb-6186-414f-a0c0-559d5bc66378.png |
| Kakao 500 g | img/baleni-kakao_holandskeho_typu.webp | https://d2ol7oe51mr4n9.cloudfront.net/user_3Bj5jSbouMgBXvv0eqo1wQl5cMI/0571c8e5-299a-4e05-8b34-b465d63d2d8b.png |

## Recipe photos

Installed 2026-09-24 (PR #37).

Still missing: real packaging photos for the dumpling mixes and sugar.
After adding: bump ASSET_VER, run build_site.py and verify_refs.py, check
product pages on phone and desktop, then open a PR.
