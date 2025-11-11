# pylint: disable=C0111
c = c  # noqa: F821 pylint: disable=E0602,C0103
config = config  # noqa: F821 pylint: disable=E0602,C0103

# === Appearance ===
c.colors.statusbar.normal.bg = "#1e1e2e"
c.colors.statusbar.command.bg = "#1e1e2e"
c.colors.statusbar.command.fg = "#cdd6f4"
c.colors.statusbar.normal.fg = "#89b4fa"
c.colors.statusbar.passthrough.fg = "#89b4fa"
c.colors.statusbar.url.fg = "#74c7ec"
c.colors.statusbar.url.success.https.fg = "#74c7ec"
c.colors.statusbar.url.hover.fg = "#89dceb"

c.colors.tabs.even.bg = "#1e1e2e"
c.colors.tabs.odd.bg = "#1e1e2e"
c.colors.tabs.bar.bg = "#1e1e2e"
c.colors.tabs.even.fg = "#6c7086"
c.colors.tabs.odd.fg = "#6c7086"
c.colors.tabs.selected.even.bg = "#cdd6f4"
c.colors.tabs.selected.odd.bg = "#cdd6f4"
c.colors.tabs.selected.even.fg = "#1e1e2e"
c.colors.tabs.selected.odd.fg = "#1e1e2e"
c.colors.tabs.indicator.start = "#a6e3a1"
c.colors.tabs.indicator.stop = "#f38ba8"
c.tabs.show = "multiple"
c.tabs.padding = {'top': 5, 'bottom': 5, 'left': 9, 'right': 9}
c.tabs.indicator.width = 0
c.tabs.width = '7%'
c.tabs.title.format = "{audio}{current_title}"

c.colors.hints.bg = "#1e1e2e"
c.colors.hints.fg = "#cdd6f4"
c.hints.border = "#cdd6f4"

c.colors.completion.odd.bg = "#1e1e2e"
c.colors.completion.even.bg = "#1e1e2e"
c.colors.completion.fg = "#cdd6f4"
c.colors.completion.category.bg = "#1e1e2e"
c.colors.completion.category.fg = "#cdd6f4"
c.colors.completion.item.selected.bg = "#1e1e2e"
c.colors.completion.item.selected.fg = "#cdd6f4"
c.colors.completion.match.fg = "#89dceb"
c.colors.completion.item.selected.match.fg = "#89dceb"

c.colors.messages.info.bg = "#1e1e2e"
c.colors.messages.info.fg = "#cdd6f4"
c.colors.messages.error.bg = "#1e1e2e"
c.colors.messages.error.fg = "#cdd6f4"

c.colors.downloads.bar.bg = "#1e1e2e"
c.colors.downloads.start.bg = "#a6e3a1"
c.colors.downloads.start.fg = "#cdd6f4"
c.colors.downloads.stop.bg = "#f38ba8"
c.colors.downloads.stop.fg = "#cdd6f4"
c.colors.downloads.error.bg = "#1e1e2e"
c.colors.downloads.error.fg = "#cdd6f4"

c.colors.tooltip.bg = "#1e1e2e"
c.colors.webpage.bg = "#1e1e2e"

# === Fonts ===
c.fonts.default_family = []
c.fonts.default_size = '12pt'
c.fonts.web.size.default = 20
c.fonts.web.family.fixed = 'monospace'
c.fonts.web.family.sans_serif = 'monospace'
c.fonts.web.family.serif = 'monospace'
c.fonts.web.family.standard = 'monospace'

# === Dark Mode ===
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.algorithm = 'lightness-cielab'
c.colors.webpage.darkmode.policy.images = 'never'
config.set('colors.webpage.darkmode.enabled', True, '*')  # Force dark mode everywhere

# === Search Engines ===
c.url.searchengines = {
    'DEFAULT': 'https://duckduckgo.com/?q={}',
    '!aw': 'https://wiki.archlinux.org/?search={}',
    '!apkg': 'https://archlinux.org/packages/?sort=&q={}&maintainer=&flagged=',
    '!gh': 'https://github.com/search?o=desc&q={}&s=stars',
    '!yt': 'https://www.youtube.com/results?search_query={}',
}

# === Completion Categories ===
c.completion.open_categories = ['searchengines', 'quickmarks', 'bookmarks', 'history', 'filesystem']

# === Session ===
c.auto_save.session = True

# === Privacy Settings ===
config.set("content.webgl", False, "*")
config.set("content.canvas_reading", False)
config.set("content.geolocation", False)
config.set("content.webrtc_ip_handling_policy", "default-public-interface-only")
config.set("content.cookies.accept", "all")
config.set("content.cookies.store", True)

# === Adblocking ===
c.content.blocking.enabled = True
# c.content.blocking.method = 'adblock'  # Uncomment if using python-adblock

# === Keybindings ===
#config.bind('=', 'cmd-set-text -s :open')
config.bind('h', 'history')
config.bind('cc', 'hint images spawn sh -c "cliphist link {hint-url}"')
config.bind('cs', 'cmd-set-text -s :config-source')
config.bind('tH', 'config-cycle tabs.show multiple never')
config.bind('sH', 'config-cycle statusbar.show always never')
config.bind('T', 'hint links tab')
config.bind('pP', 'open -- {primary}')
config.bind('pp', 'open -- {clipboard}')
config.bind('pt', 'open -t -- {clipboard}')
config.bind('qm', 'macro-record')
config.bind('<ctrl-y>', 'spawn --userscript ytdl.sh')
config.bind('tT', 'config-cycle tabs.position top left')
config.bind('gJ', 'tab-move +')
config.bind('gK', 'tab-move -')
config.bind('gm', 'tab-move')
config.bind('=' , 'zoom-in')
config.bind('0' , 'zoom 100')
# === Autoconfig ===+
config.load_autoconfig()

