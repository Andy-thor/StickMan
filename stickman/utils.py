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

import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf
from stickman.locals import *

def load_new_pixbuf(toon):
    orientation = "-{}".format(toon.orientation) if (toon.current_action != "base") else ""
    # Load the pixbuf
    pixbuf = load_pixbuf_from_file(DATADIR + DIR_IMAGES + APP_NAME.lower() + "-{}{}{}.png".format(
                                    toon.current_action, orientation, toon.current_frame))
    return pixbuf


def load_pixbuf_from_file(path):
    pixbuf = GdkPixbuf.Pixbuf.new_from_file(path)
    return pixbuf


def get_resolution_width():
    return Gdk.Screen.get_default().get_width()


def get_resolution_height():
    return Gdk.Screen.get_default().get_height()


def get_resolution():
    width = get_resolution_width()
    height = get_resolution_height()
    return (width, height)
