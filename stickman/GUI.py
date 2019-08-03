# -*- coding: UTF-8 -*-
#
#  StickMan
#  Copyright (C) 2019 Andrés Segovia
#  
#  StickMan is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys
import os
import time
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GObject
try:
    import cairo
    gi.require_foreign("cairo")
except ImportError:
    from gi.repository import cairo # pycairo
    print("No cairo integration.")
import stickman.utils as utils
from stickman.locals import *

# =============================
# The Window
# =============================
class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, Gtk.WindowType.POPUP)
        self.set_events(self.get_events() | Gdk.EventMask.BUTTON_PRESS_MASK)
        self.set_decorated(False)
        self.set_size_request(20, 20) # The widget size will then be adjusted to the size of the image.
        self.connect('destroy', Gtk.main_quit)
        self.connect('draw', self.draw)

        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual and screen.is_composited():
            self.set_visual(visual)
        self.set_app_paintable(True)

        self.x_pos = int(utils.get_resolution_width() / 2)
        self.y_pos = utils.get_resolution_height() - 108 # The value subtracted is to accommodate the image.
        self.move(self.x_pos, self.y_pos)
        self.image = Gtk.Image()
        self.fixed = Gtk.Fixed()
        self.fixed.put(self.image, 0, 0)
        
        self.menu = Gtk.Menu()
        lbl_menu_item = ["About...", "Exit"]
        for label in lbl_menu_item:
            menu_items = Gtk.MenuItem(label)
            self.menu.append(menu_items)
            # When there is an event on the MenuItem (in this case left click)
            menu_items.connect("activate", self.clicked_item, label)
            menu_items.show()
        # When there is an event on the toon (in this case right click)
        self.connect("button_press_event", self.on_clicked, self.menu)
        self.add(self.fixed)
        self.show_all()

    def draw(self, widget, context):
        context.set_source_rgba(0, 0, 0, 0)
        context.set_operator(cairo.OPERATOR_SOURCE)
        context.paint()
        context.set_operator(cairo.OPERATOR_OVER)

    def update(self, toon):
        pixbuf = utils.load_new_pixbuf(toon)
        self.image.set_from_pixbuf(pixbuf)
        self.image.show()
        self.fixed.set_size_request(100, 100)
        self.fixed.show()
        self.x_pos += toon.sideways()
        self.move(self.x_pos, self.y_pos)
        Gtk.Widget.show(self.image)
        self.show()
    
    # This is for capturing events on the widget
    def on_clicked(self, arg, event, menu): # We don't use 'arg' in this case(Fix)
        if event.type == Gdk.EventType.BUTTON_PRESS and event.button == 3:
            event.button = 1
            menu.popup(None, None, None, None, event.button, event.time)
    
    def clicked_item(self, arg, text): # We don't use 'arg' in this case(Fix)
        if text == "About...":
            about = About(self)
            about.run()
            about.destroy()
        else: # Exit
            Gtk.main_quit()
            sys.exit()

class About(Gtk.AboutDialog):
    def __init__(self, parent):
        Gtk.AboutDialog.__init__(self, transient_for=parent, modal=True)
        authors = [AUTHOR]
        develop_year = 2019
        current_year = time.strftime("%Y")
        time_lapse = develop_year # -> For example: 2019-2020
        if int(current_year) > develop_year:
            time_lapse = f"{develop_year}-{current_year}"
        self.set_authors(authors)
        self.set_license(LICENSE)
        self.set_program_name(APP_NAME)
        self.set_version("0.2.3")
        self.set_copyright(f"Copyright © {time_lapse} {authors[0].split('<')[0]}")
        self.set_comments("A little toon that moves on your desktop")
        self.set_website("https://andy-thor.github.io/StickMan")
        self.set_website_label("Visit StickMan Homepage")
        self.set_logo(utils.load_pixbuf_from_file(os.path.join(DATADIR, DIR_ICONS, APP_NAME.lower() + ".png")))