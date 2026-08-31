Jůzlová.cz — local copy on this Mac

1. Unzip the download. You should see a folder named
   juzlova-rebuild-status-main (or similar).
2. Open that folder, then open the local-mac folder.
3. Double-click "Open Juzlova locally.command".
   The site opens at http://127.0.0.1:8765/
4. Leave the Terminal window open while you browse.
   Close it when you are done.

If macOS says the file cannot be opened:
  Right-click "Open Juzlova locally.command" → Open → Open.

To refresh later, in Terminal:

  cd ~/Downloads/juzlova-rebuild-status-main
  git pull

Or clone a living copy:

  cd ~/Documents
  git clone https://github.com/adamripon-ship-it/juzlova-rebuild-status.git juzlova.cz
