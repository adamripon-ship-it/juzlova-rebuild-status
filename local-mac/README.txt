Jůzlová.cz — local copy on this Mac

Your copy lives at:
  /Users/adam/juzlova-site/juzlova-rebuild-status-cursor-mac-local-download-ddb7

Port 8765 is often already taken. Use 8770, or double-click
"Open Juzlova locally.command" in the unzipped site folder
(it picks a free port for you).

In Terminal, paste this whole block:

  cd /Users/adam/juzlova-site/juzlova-rebuild-status-cursor-mac-local-download-ddb7
  open http://127.0.0.1:8770/
  python3 -m http.server 8770 --bind 127.0.0.1

Leave that window open. The site is at http://127.0.0.1:8770/

If macOS says the .command file cannot be opened:
  Right-click it → Open → Open.
