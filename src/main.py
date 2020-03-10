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

import os, random
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GObject
from stickman import locals_constants, utils
from stickman.widgets import Window
from stickman.models import Toon

# Function that will constantly update the objects
def main_loop(widget, toon):
    # We update its properties
    toon.update(widget)
    widget.update(toon)
    return True

# Main function
def main():
    stickman = Toon()
    widget = Window()
    GObject.timeout_add(locals_constants.TIMEOUT_RATE_FRAMES, main_loop, widget, stickman)
    return 0
