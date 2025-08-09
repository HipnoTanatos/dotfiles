from datetime import datetime
from libqtile.config import Key, Drag, Click
from libqtile.lazy import lazy
from settings.groups import groups
# from opp import opacity_up, opacity_down


terminal = "alacritty"
mod = "mod4"
keymap = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod, "shift"], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(), lazy.hide_show_bar("top"),
        desc="Toggle fullscreen on the focused window",
    ),

    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),


    # """
    # Applications
    # """
    Key([mod], "m", lazy.spawn("rofi -show drun")),
    Key([mod, "shift"], "m", lazy.spawn("rofi -show")),

    Key([mod], "b", lazy.spawn("firefox")),

    Key([mod], "e", lazy.spawn("alacritty -e ranger")),
    #Key([mod, "shift"], "Return", lazy.spawn("alacritty -e ipython")),
    Key([mod], "z", lazy.spawn("zathura")),

    # """
    # Media Player
    # """
    #TODO: implement a mute toggle comand
    # Key([], "XF86AudioMute", lazy.spawn(
    #     "wpctl set-mute @DEFAULT_AUDIO_SINK@ 1"
    # )),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "wpctl set-volume @DEFAULT_AUDIO_SINK@ 1%-"
    )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "wpctl set-volume @DEFAULT_AUDIO_SINK@ 1%+"
    )),

    Key([], "XF86AudioPlay", lazy.spawn(
        "playerctl play-pause"
    )),
    Key([], "XF86AudioStop", lazy.spawn(
        "playerctl stop"
    )),

    Key([], "XF86AudioNext", lazy.spawn(
        "playerctl next"
    )),
    Key([], "XF86AudioPrev", lazy.spawn(
        "playerctl previous"
    )),

    Key(["control"], "XF86AudioNext", lazy.spawn(
        "playerctl position 5+"
    )),
    Key(["control"], "XF86AudioPrev", lazy.spawn(
        "playerctl position 5-"
    )),

    # """
    # Misc
    # """
    # Opacity
    # Key([mod], "XF86AudioLowerVolume", opacity_down(1)),
    # Key([mod], "XF86AudioRaiseVolume", opacity_up(1)),

    # Screen control
    Key([mod], "Tab", lazy.next_screen()),

    # Key([], "Print", lazy.spawn(f"maim /home/HipnoTanatos/Screenshots/{datetime.now().strftime('%d-%m-%Y_%H:%M:%S')}.png")),
    #Key([], "Print", lazy.spawn("maim -s | xclip -selection clipboard -t image/png")),
    Key([], "Print", lazy.spawn("upload_screenshot")),
    Key([mod], "d", lazy.spawn("qtile run-cmd -g 2 -f alacritty")),
]

mousemap = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

for i in groups:
    keymap.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
