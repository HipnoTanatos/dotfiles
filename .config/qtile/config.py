from libqtile import bar, layout, qtile, widget
from libqtile.bar import Bar
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

import maps
from settings.groups import groups
from settings.layouts import layouts

keys = maps.keymap
mouse = maps.mousemap

widget_defaults = dict(
    font="JetBrains Nerd Font Mono",
    fontsize=12,
    padding=5,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(highlight_method='text',
                                active="#ffffff",
                                this_current_screen_border='#d79920',
                                use_mouse_wheel=False,
                                font="JetBrains Nerd Font Mono",
                                fontsize=23,
                                padding=10,
                                diable_drag=True
                                ),
                widget.Spacer(),
                # widget.WindowName(),
                # widget.Spacer(),
                # widget.TaskList(),
                widget.CurrentLayoutIcon(scale=0.7),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(),
                widget.Clock(format="%a %d-%m %I:%M %p"),
                widget.Spacer(length=3),
            ],
            30,
            margin=[6, 150, 6, 150],
            background='#282828',
            border_width=[1, 0, 1, 0],  # Draw top and bottom borders
            border_color="#ddc7a1",  # Borders are magenta
        ),

        left=bar.Gap(5),
        right=bar.Gap(5),
        bottom=bar.Gap(6),

        wallpaper='~/Pictures/Wallpapers/water_rock_grain_0_100.jpg',
        wallpaper_mode='fill',
        x11_drag_polling_rate = 60,
    ),
    Screen(
        wallpaper='~/Pictures/Wallpapers/water_rock_grain_0_100.jpg',
        wallpaper_mode='fill',
    )
]

# Drag floating layouts.


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_width=1,
    border_focus='#ac9e83', border_normal='#928374',
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="Blender Preferences"),
        Match(title="Media viewer"),
    ]
)
auto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False
wl_input_rules = None
wmname = "LG3D"
