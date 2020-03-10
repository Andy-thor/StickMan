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

APP_NAME = "StickMan"
VERSION = "0.2.4"
AUTHOR = 'Andrés Segovia <andy.dev536@gmail.com>'
_parent_dir = os.path.dirname(os.path.abspath(__file__))
_separator = os.path.sep
if _parent_dir.split(_separator)[-1] == "src":
    DATADIR = os.path.join(os.path.dirname(_parent_dir) + '/')
else:
    _prefix = "usr"
    DATADIR = os.path.join(_prefix, "share", APP_NAME.lower() + '/')
DIR_IMAGES = 'data/images/'
DIR_ICONS = 'data/icons/'
TIMEOUT_RATE_FRAMES = 50 # 1 frame/50ms -> 20 fps
LICENSE = """
StickMan
Copyright © 2019 Andrés Segovia

This is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
