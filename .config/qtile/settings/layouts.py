from libqtile import bar, layout, qtile, widget


layouts = [
    layout.Columns(border_width = 1, margin = 4, border_on_single = True,
                   border_focus = '#ddc7a1', border_normal = '#928374',
                   border_focus_stack = '#ddc7a1', border_normal_stack = '#ac9e83',
                   initial_ratio = 1.91, insert_position = 1, split = False,
                   grow_amount = 0.943),
    # initial_ratio 1.4

    # layout.Max(),

    # layout.Columns(border_width = 1, margin = [ 12, 9, 9, 9 ], border_on_single = True,
    #                border_focus = '#ddc7a1', border_normal = '#928374',
    #                border_focus_stack = '#ddc7a1', border_normal_stack = '#ac9e83',
    #                initial_ratio = 1.60, insert_position = 1, split = False,
    #                grow_amount = 11),

    layout.Columns(border_width = 1, margin = [45, 84, 56, 84], border_on_single = True,
                   border_focus = '#ddc7a1', border_normal = '#928374',
                   border_focus_stack = '#ac9e83', border_normal_stack = '#928374',
                   insert_position = 1, split = False,
                   grow_amount = 11),

    layout.Columns(border_width = 1, margin = [ 0, 0, 0, 0 ], border_on_single = True,
                   border_focus = '#ddc7a1', border_normal = '#928374',
                   border_focus_stack = '#ddc7a1', border_normal_stack = '#ac9e83',
                   initial_ratio = 1.60, insert_position = 1, split = False,
                   grow_amount = 3),

   #layout.MonadTall(border_width=1, ratio=0.61, margin=5,
   #                 border_focus='#d79921', border_normal='#928374'),
   #layout.Max(boder_width=0, margin=0, border_normal='#928374', border_focus='#ddc7a1'),


    # Try more layouts by unleashing below layouts.
   #layout.Stack(autosplit=True, border_width=1, margin = 5,
   #             border_focus = '#d79921', border_normal = '#928374',),
   #layout.Bsp(border_width=2, ratio=0.6, margin=5,
   #           border_focus='#d79921', border_normal='#928374'),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
   #layout.Tile(),
   #layout.TreeTab(),
    # layout.VerticalTile(),
   #layout.Zoomy(),
]
