return {

  "folke/snacks.nvim",
  --@type snacks.Config,
  opts = {
    dashboard = {
      sections = {
        {
          pane = 1,
          section = "terminal",
          cmd = "chafa /home/jamar/Documents/Scripts/AsuraScrape/most-recent.webp --size 60x60 --symbols sextant",
          height = 25,
          padding = 1,
          ttl = 60 * 5,
        },
        { pane = 2, icon = " ", title = "Recent Files", section = "recent_files", indent = 2, padding = 1 },
        { pane = 2, icon = " ", title = "Projects", section = "projects", indent = 2, padding = 1 },
        {
          pane = 2,
          icon = "🕮",
          title = "Recent Updates",
          section = "terminal",
          cmd = "python /home/jamar/Documents/Scripts/AsuraScrape/getRecentManhua.py",
          padding = 1,
          ttl = 60 * 5,
          indent = 5,
        },
        {
          pane = 2,
          icon = " ",
          title = "Git Status",
          section = "terminal",
          enabled = function()
            return Snacks.git.get_root() ~= nil
          end,
          cmd = "git status --short --branch --renames",
          height = 5,
          padding = 1,
          ttl = 5 * 60,
          indent = 3,
        },
        { section = "startup" },
      },
    },
  },
}
