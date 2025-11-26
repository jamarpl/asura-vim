# asura-vim
just a snacks.nvim config that shows recently updated manhwa on your dashboard


## Installation
### Python Requirements: requests, BeautifulSoup4, json
If you only want to include the scripts in your own setup, just copy them and replace the file locations to wherever you prefer them to be. I recommend making a folder just for the scripts, image, and json so that everything is contained.

---
<img width="1317" height="776" alt="image" src="https://github.com/user-attachments/assets/f18dbe2a-7051-45fb-8333-37575d60d6a9" />
<br/>
<br/>

**Step 1:** Clone the repository and move the python scripts to your desired location.

**Step 2:** Change the file names within the scripts to the location you selected. Ensure you use full paths (no ~) to ensure consistency.

**Step 3:** Make a cronjob (using cronie if you're on arch) set to run the asuraScrape script automatically (15 minutes is recommended, no need to call so often).

**Step 4:** Install snacks.nvim using your plugin manager. If you're using LazyVim, snacks.nvim should already be installed.

**Step 5:** Place `dashboard.lua` in `~/.config/nvim/lua/plugins/`. This will override the default dashboard. If you already have another dashboard plugin running, be sure to disable it.

**Step 6:** Change the chafa command to the picture location, and change the Recent Chapters command to the `getRecentChapters.py` location. snacks.nvim caches their results automatically, so you can set `ttl=0` to while testing to make sure the update is reflecting. I suggest setting `ttl =< <cronjob interval>` so that you don't miss any updates.

**Step 7:** Test it out! If you have any problems, check out the snacks.nvim documentation, and if that doesn't help raise an issue.

## Notes
_Also, I know the bs4 query could be optimized very slightly. Make a pull request if you feel like changing it (hehe_)
