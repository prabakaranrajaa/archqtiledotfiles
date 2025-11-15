import os

import subprocess
import libqtile.resources
from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import colors
import random

# Your list of options
any_list = ["DoomOne", "Dracula", "GruvboxDark", "MonokaiPro",  "Nord","OceanicNext", "Palenight", "SolarizedDark", "SolarizedLight", "TomorrowNight", "TokyoNight", "TokyoNight"]

# Pick one randomly
chosen = random.choice(any_list)

colors = getattr(colors, chosen)
#colors = colors.Dracula

mod = "mod4"
#terminal = guess_terminal()
mod = "mod4"              # Sets mod key to SUPER/WINDOWS
terminal = "kitty"      # My terminal of choice
myBrowser = "qutebrowser"       # My browser of choice

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.spawn("rofi -show drun -show-icons"), desc='Run Launcher'),
    
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.spawn(myBrowser), desc='Web browser'),
    Key([mod], "b", lazy.hide_show_bar(position='all'), desc="Toggles the bar to show/hide"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control", "shift"], "q", lazy.spawn("qtile cmd-obj -o cmd -f shutdown"), desc="Logout menu"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control", "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    
    Key([mod, "control","mod1"], "up", lazy.spawn("xrandr -o 0"), desc="Window drection up"),
    Key([mod, "control","mod1"], "left", lazy.spawn("xrandr -o 1"), desc="Window drection left"),
    Key([mod, "control","mod1"], "down", lazy.spawn("xrandr -o 2"), desc="Window drection down"),
    Key([mod, "control","mod1"], "right", lazy.spawn("xrandr -o 3"), desc="Window drection right"),
    
    
    KeyChord([mod], "o", [
        Key([], "b", lazy.spawn("brave")),
        Key([], "f", lazy.spawn("pcmanfm")),
    ], name="launch")
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# Uncomment only one of the following lines
group_labels = ["", "", "👁", "", "", "", "✀", "꩜", "", "⎙"]
#group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
#group_labels = ["DEV", "WWW", "SYS", "DOC", "VBOX", "CHAT", "MUS", "VID", "GFX", "MISC"]

group_layouts = ["monadtall"] * 10

groups = [Group(name=n, label=l, layout=lay) for n, l, lay in zip(group_names, group_labels, group_layouts)]

keys.extend(
        [
    Key([mod], g.name, lazy.group[g.name].toscreen(), desc=f"Switch to group {g.name}") for g in groups
] + [
    Key([mod, "shift"], g.name, lazy.window.togroup(g.name), desc=f"Move window to group {g.name}") for g in groups
]
    )
    
layout_theme = {"border_width": 2,
                "margin": 3,
                "border_focus": "ff00ff",
                "border_normal": colors[0]
                }

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    layout.Stack(num_stacks=2),
    layout.Bsp(**{"border_width": 2,"margin": 3}),
    layout.Matrix(**{"border_width": 2,"margin": 3}),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**{"border_width": 2,"margin": 3}),
    layout.RatioTile(**{"border_width": 2,"margin": 3}),
    layout.Tile(**{"border_width": 2,"margin": 3}),
    layout.TreeTab(**{"border_width": 2,"margin": 3}),
    layout.VerticalTile(**{"border_width": 2,"margin": 3}),
    layout.Zoomy(**{"border_width": 2,"margin": 3}),
]

widget_defaults = dict(
    font="JetBrains Mono NF",
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

battery = widget.Battery(
    format='{char}{percent:2.0%} ',
    charge_char='🔌',
    discharge_char='🔋',
    empty_char='⚡',
    full_char='✅',
    update_interval=30,
    low_percentage=20,
    notify_below=20,
    show_short_text=False,
    foreground='#ffffff',
    low_foreground='#ff5555',
    full_foreground='#50fa7b',
    notification_timeout=5,
    notification_script="paplay /usr/share/sounds/freedesktop/stereo/suspend-error.oga"
)


# --- Play / Pause / Stop icon ---
play_icon = widget.TextBox(
    fontsize=18,
    foreground="#00ff00",
    text="▶️",  # start with Play
)

def rmpc_notify_with_icon(cmd, icon_widget):
    try:
        # Run the command
        subprocess.run(["mpc", "-h", "localhost", "-p", "6601", cmd], check=True)

        # Get status and song
        status = subprocess.run(
            ["mpc", "-h", "localhost", "-p", "6601", "status"],
            capture_output=True, text=True, check=True
        ).stdout
        song = subprocess.run(
            ["mpc", "-h", "localhost", "-p", "6601", "current"],
            capture_output=True, text=True, check=True
        ).stdout.strip()

        # Update icon based on state
        if "[playing]" in status:
            icon_widget.update("▶️")   # Play icon
            subprocess.run(["dunstify", "-a", "MPD", "-r", "1234",
                            "▶️ Now Playing", song, "-i", "media-playback-start"])
        elif "[paused]" in status:
            icon_widget.update("⏸️")   # Pause icon
            subprocess.run(["dunstify", "-a", "MPD", "-r", "1234",
                            "⏸️ Paused", song, "-i", "media-playback-pause"])
        else:
            icon_widget.update("⏹️")   # Stop icon
            subprocess.run(["dunstify", "-a", "MPD", "-r", "1234",
                            "⏹️ Stopped", "No track playing", "-i", "media-playback-stop"])
    except subprocess.CalledProcessError:
        icon_widget.update("⚠️")
        subprocess.run(["dunstify", "-a", "MPD", "-r", "1234",
                        "⚠️ Error", "MPD command failed"])

# Attach callbacks
play_icon.add_callbacks({
    "Button1": lambda: rmpc_notify_with_icon("play", play_icon),   # Left click → Play
    "Button2": lambda: rmpc_notify_with_icon("stop", play_icon),   # Middle click → Stop
    "Button3": lambda: rmpc_notify_with_icon("pause", play_icon),  # Right click → Pause
})


# --- Skip icon: Previous / Next ---
skip_icon = widget.TextBox(
    fontsize=18,
    foreground="#ff00ff",
    text="⏭️",  # default icon
)

def rmpc_skip(cmd, icon_widget):
    try:
        subprocess.run(["mpc", "-h", "localhost", "-p", "6601", cmd], check=True)

        song = subprocess.run(
            ["mpc", "-h", "localhost", "-p", "6601", "current"],
            capture_output=True, text=True, check=True
        ).stdout.strip()

        if cmd == "next":
            icon_widget.update("⏭️")  # Next icon
            subprocess.run(["dunstify", "-a", "MPD", "-r", "1234",
                            "⏭️ Next Song", song, "-i", "media-skip-forward"])
        elif cmd == "prev":
            icon_widget.update("⏮️")  # Previous icon
            subprocess.run(["dunstify", "-a", "MPD", "-r", "1234",
                            "⏮️ Previous Song", song, "-i", "media-skip-backward"])
    except subprocess.CalledProcessError:
        icon_widget.update("⚠️")
        subprocess.run(["dunstify", "-a", "MPD", "-r", "1234",
                        "⚠️ Error", "MPD command failed"])

# Attach callbacks (fixed mapping)
skip_icon.add_callbacks({
    "Button1": lambda: rmpc_skip("next", skip_icon),   # Left click → Previous
    "Button3": lambda: rmpc_skip("prev", skip_icon),   # Right click → Next
})



#logo = os.path.join(os.path.dirname(libqtile.resources.__file__), "logo.png")
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(
                 filename = "~/.config/qtile/icons/p.png",
                 scale = "False",
                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("rofi -show drun -show-icons")},
                 ),
                widget.Prompt(),
                widget.GroupBox(
                 fontsize = 16,
                 #padding_x = 6,
                 padding_y = 6,
                 active = colors[4],
                 #inactive = colors[9],
                 rounded = True,
                 highlight_color = colors[3],
                 highlight_method = "line",
                 
                ),
                widget.TextBox(
                 text = '|',
                 font = "JetBrains Mono NF",
                 foreground = colors[9],
                 padding = 2,
                 fontsize = 20
                 ),
                widget.LaunchBar(
                 progs = [("🦁", "brave", "Brave web browser"),
                          ("🚀", "kitty", "Kitty terminal"),
                          ("📁", "pcmanfm", "PCManFM file manager"),
                          ("🎸", "vlc", "VLC media player")
                         ], 
                 fontsize = 20,
                 padding = 2,
                 foreground = colors[3],
        	),
        	widget.TextBox(
                 text = '|',
                 font = "JetBrains Mono NF",
                 foreground = colors[9],
                 padding = 2,
                 fontsize = 20
                 ),
                widget.CurrentLayout(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(),
                
               

                
	widget.Net(
        	foreground = colors[3],
    		#format="{down:6.2f}{down_suffix:<2}↓↑{up:6.2f}{up_suffix:<2}",
    		format='{down:.0f}{down_suffix}↓ ↑{up:.0f}{up_suffix}',
    		interface="wlan0",  # Change to your actual network interface
    		update_interval=1,
    		use_bits=False,
    		prefix=None,
    		cumulative_prefix=None,
		),
	widget.GenPollText(
    		func=lambda: subprocess.getoutput("python3 ~/.config/qtile/scripts/net_usage.py"),
    		fmt = '{}',
    		update_interval=60,
    		foreground=colors[8]
		),
	widget.CPU(
                 foreground = colors[4],
                 #padding = 8, 
                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                 format = '{load_percent}%',
                 ),
        widget.Memory(
                 foreground = colors[8],
                 #padding = 8, 
                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                 format = '{MemUsed:.0f}{mm}',
                 fmt = '🖥{}',
                 ),
        widget.DF(
                 update_interval = 60,
                 foreground = colors[5],
                 #padding = 8, 
                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('/home/karan/.config/qtile/scripts/notify-disk')},
                 partition = '/',
                 #format = '[{p}] {uf}{m} ({r:.0f}%)',
                 format = '{uf}{m}',
                 fmt = '🖴{}',
                 visible_on_warn = False,
                 ),
                 play_icon,
                 skip_icon,

        widget.Volume(
                 foreground = colors[7],
                 #padding = 8, 
                 fmt = '🕫{}',
                 ),
                
 #battery,   # <--- use the variable here
 widget.GenPollText(
    func=lambda: subprocess.getoutput("~/.config/qtile/scripts/battery_alert.sh"),
    update_interval=30,
    foreground='#ffffff'
),
                #widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.Clock(foreground = colors[8], format="%S %I:%M"),
                #widget.QuickExit(),
                widget.QuickExit(
    default_text='⏻',  # Unicode power icon
    countdown_format='[{}]',  # Optional: shows countdown before exit
    padding=10,
    fontsize=18,
    foreground='ff5555',  # Optional: red color
)
            ],
            26,
            #border_width=[1, 0, 1, 0],  # Draw top and bottom borders
            #border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        background="#000000",
        wallpaper="~/Pictures/Wallpapers/kill.jpeg",
        wallpaper_mode="fill",       #center",
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
focus_previous_on_window_remove = False
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

@hook.subscribe.startup_once
def start_once():
	home = os.path.expanduser('~')
	subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])
	#subprocess.Popen([home + '/.config/qtile/scripts/mpd-notify.sh'], shell=True)

	subprocess.Popen(["nm-applet"])
	subprocess.Popen(["copyq"])
#	subprocess.Popen(["xrandr", "--output", "eDP-1", "--same-as", "HDMI-1"])
#	subprocess.Popen(["xinput", "set-button-map", "15", "3", "2", "1"])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
