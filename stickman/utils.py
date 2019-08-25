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
import json
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf
from stickman.locals_constants import *

colors = {"red": "\033[31m", "green": "\033[32m", "blue": "\033[34m", "none": "\033[0m"}


def load_new_pixbuf(src_img):
    src_path = os.path.join(DATADIR, DIR_IMAGES, APP_NAME.lower() + src_img)
    pixbuf = load_pixbuf_from_file(src_path)
    return pixbuf


def load_pixbuf_from_file(path):
    pixbuf = GdkPixbuf.Pixbuf.new_from_file(path)
    return pixbuf


def load_data_json(file_name="data_actions.json"):
        try:
            path_file = os.path.join(DATADIR, 'src', file_name)
            with open(path_file, "r") as file_json:
                data = file_json.read()
        except IOError:
            print(f"{colors['red']}File '{file_name}' does not exists{colors['none']}")
            sys.exit()
        else:
            parsed_data = json.loads(data)
            return parsed_data


def get_resolution_width():
    return Gdk.Screen.get_default().get_width()


def get_resolution_height():
    return Gdk.Screen.get_default().get_height()


def get_resolution():
    width = get_resolution_width()
    height = get_resolution_height()
    return (width, height)
