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
import random
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
from stickman.locals_constants import *


class Action(object):
    """This defines the actions for the model"""
    def __init__(self, action_name="base"):
        self.all_actions = utils.load_data_json()
        self.select_new_action(new_name=action_name)

    def select_new_action(self, new_name=None, new_orientation=None):
        self.action_name = new_name or random.choice(self.current_action["next_actions"])
        self.current_action = self.all_actions[self.action_name]
        self.orientation = new_orientation or random.choice(self.all_actions["orientations"])
        self._current_frame = 0 # Number to be exchanged between the sprites

    def change_orientation(self, x_pos):
        """This is to prevent it does not exceed the limits of the screen"""
        if x_pos > utils.get_resolution_width():
            self.select_new_action(new_name="run", new_orientation="left")
        else:
            self.select_new_action(new_name="run", new_orientation="right")

    @property
    def n_frames(self):
        return self.current_action["n_frames"]

    @property
    def current_frame(self):
        return self._current_frame

    @current_frame.setter
    def current_frame(self, value):
        self._current_frame = value

    def get_name(self):
        return self.action_name

    def update_frames(self):
        self._current_frame += 1


class ModelBase():
    def __init__(self):
        self.all_actions = utils.load_data_json()
    
    def calculate_advance(self):
        """This calculates how many pixels it has to advance"""
        pass

    def update(self, widget):
        """This method constantly frames"""
        pass


# =============================
# Toon
# =============================
class Toon(ModelBase):
    def __init__(self):
        ModelBase.__init__(self)
        action_name = tuple(self.all_actions.keys())[0] # -> base
        self.action = Action(action_name) # Current action
        
    def calculate_advance(self):
        """This calculates how many pixels it has to advance"""
        action_name = self.action.get_name()
        if action_name == "run":
            advance = 20
        elif action_name == "stop":
            advance = 15
        elif action_name in ["walk", "go"]:
            advance = 10
        else:
            advance = 0

        if self.action.orientation == "left":
            advance = -advance
        return advance
    
    def update(self, widget):
        """This method constantly frames"""
        current_frame = self.action.current_frame
        num_frames = self.action.n_frames
        if current_frame == num_frames - 1:
            if widget.x_pos > utils.get_resolution_width() or widget.x_pos < 0:
                self.action.change_orientation(widget.x_pos)
            else:
                self.action.select_new_action()
        else:
            self.action.update_frames()
