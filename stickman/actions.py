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
import sys
import json
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from random import randrange
from stickman.locals_constants import *

orientations = ['right', 'left']
try:
    file_name = "data_actions.json"
    path_file = os.path.join(DATADIR, 'src', file_name)
    with open(path_file, "r") as file_json:
        data = file_json.read()
except IOError:
    print(f"\033[31m'{file_name}' file does not exist\033[0m")
    sys.exit()
else:
    all_actions = json.loads(data)

def set_new_action(toon):
    action = toon.current_action
    new_action = choose_action(action)
    new_num_frames = number_of_frames(new_action)
    
    # To choose the direction to move
    if new_action == 'base':
        toon.orientation = orientations[randrange(len(orientations))]
    
    # Updating toon actions
    toon.current_action = new_action
    toon.num_frames = new_num_frames

def choose_action(action):
    size_list = len(all_actions[action]["next_actions"])
    next_action = all_actions[action]["next_actions"][randrange(size_list)]
    return next_action

def number_of_frames(action):
    n_frames = all_actions[action]["n_frames"]
    return n_frames
