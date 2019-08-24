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
from stickman import locals_constants, actions, utils
from stickman.widgets import Window
# =============================
# Toon
# =============================
class Toon:
    def __init__(self):
        self.current_action = tuple(actions.all_actions.keys())[0] # -> base
        self.orientation = actions.orientations[random.randrange(len(actions.orientations))]
        self.current_frame = 0  # Number to be exchanged between the Sprites
        self.num_frames = 5     # Number that compose the Sprites of the current action
    
    # We use it to move the widget to the sides
    def sideways(self):
        if self.current_action == "run":
            distance = 20
        elif self.current_action == "stop":
            distance = 15
        elif self.current_action in ["walk", "go"]:
            distance = 10
        else:
            distance = 0
        
        # If the orientation is to the left 
        # we will try to make its value negative.
        if self.orientation == "left":
            distance = -(distance)
        
        return distance
    
    # This is to prevent it from going beyond the limits of the screen.
    def change_orientation(self, x_pos):
        if x_pos > utils.get_resolution_width():
            self.current_action = "run"
            self.num_frames = 6
            self.orientation = "left"
        elif x_pos < 0:
            self.current_action = "run"
            self.num_frames = 6
            self.orientation = "right"
    
    def update(self, widget):
        # To check if they used all the frames of the current action
        if self.current_frame == self.num_frames - 1:
            self.current_frame = 0
            
            if widget.x_pos > utils.get_resolution_width() or widget.x_pos < 0:
                self.change_orientation(widget.x_pos)
            else:
                actions.set_new_action(self)
        else:
            self.current_frame += 1

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
