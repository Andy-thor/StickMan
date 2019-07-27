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

import sys, time
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GObject
import cairo
import utils
from locals import *

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
        for i in range(2):
            menu_items = Gtk.MenuItem(lbl_menu_item[i])
            self.menu.append(menu_items)
            # When there is an event on the MenuItem (in this case left click)
            menu_items.connect("activate", self.clicked_item, lbl_menu_item[i])
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
        #pixmap, mask = pixbuf.render_pixmap_and_mask()
        #self.image.set_from_pixmap(pixmap, mask)
        self.image.set_from_pixbuf(pixbuf)
        self.image.show()
        self.fixed.set_size_request(100, 100)
        self.fixed.show()
        #self.shape_combine_mask(mask, 0, 0)
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
            authors = [AUTHOR]
            develop_year = 2019
            current_year = time.strftime("%Y") # To determine the current year
            if int(current_year) > develop_year:
                time_lapse = "{}-{}".format(develop_year, current_year)
            else:
                time_lapse = str(develop_year)
            
            about = Gtk.AboutDialog()
            about.set_authors(authors)
            about.set_license(LICENSE)
            about.set_program_name(APP_NAME)
            about.set_version("0.1")
            about.set_copyright("Copyright © {} {}".format(time_lapse, authors[0].split("<")[0]))
            about.set_comments("A little toon that moves on your desktop")
            about.set_website("https://andy-thor.github.io/StickMan")
            about.set_website_label("Visit StickMan Homepage")
            about.set_logo(utils.load_pixbuf_from_file(DATADIR + DIR_ICONS + APP_NAME.lower() + ".png"))
            about.run()
            about.destroy()
        else:   # Exit
            Gtk.main_quit()
            sys.exit()
