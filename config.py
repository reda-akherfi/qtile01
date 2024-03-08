from settings.keys import keys, mod
from settings.groups import groups
from settings.layoutus import layouts, floating_layout
from settings.widgets import widget_defaults, screens, extension_defaults
from settings.mousimus import mouse

import os 
import subprocess
from libqtile import hook

terminal = "alacritty"



@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

@hook.subscribe.client_new
def new_client(client):
    if client.name == "alacritty":
        client.togroup("1")

main = None
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
