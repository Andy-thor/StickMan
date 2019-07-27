#!/usr/bin/env python
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
import shutil
import glob

from distutils.core import setup
from distutils.command.install import install

class CustomInstall(install):
    def run(self):
        install.run(self)
        # This copy the script and the binary script in their respective destinations
        src_script = os.path.join(os.getcwd(), self.distribution.get_name().lower() + ".py")
        script_path = os.path.join(self._custom_data_dir, self.distribution.get_name().lower() + ".py")
        shutil.copy(src_script, script_path)
        
        src_bin = os.path.join(os.getcwd(), "bin", self.distribution.get_name().lower() + ".sh")
        bin_path = os.path.join(self.prefix, "bin", self.distribution.get_name().lower())
        shutil.copy(src_bin, bin_path)
        os.chmod(script_path, 0o755)
        os.chmod(bin_path, 0o755)
        
        # This is a script created by the Setup on /usr/local/bin/ 
        # but it is better to put it on /usr/games, because of it I delete it
        path_rmv = os.path.join(self.prefix, "local", 
                                "bin", self.distribution.get_name().lower() + ".py")
        os.remove(path_rmv)
        
        # Put the icon path, and save the .desktop file where it should be
        src_desktop = os.path.join(os.getcwd(), "src", self.distribution.get_name().lower() + '.desktop')
        dst_desktop = os.path.join(self._custom_apps_dir)
        src_icon = os.path.join(os.getcwd(), 'src', 'icons', self.distribution.get_name().lower() + '.png')
        shutil.copy(src_desktop, dst_desktop)
        shutil.copy(src_icon, self._custom_icon_dir)
        
        # This put the 'src' folder where it should be, in the folder project
        if not os.path.exists(os.path.join(self._custom_data_dir, 'src', 'icons')):
            os.makedirs(self._custom_data_dir + "/src/icons")
        if not os.path.exists(os.path.join(self._custom_data_dir, 'src', 'images')):
            os.makedirs(self._custom_data_dir + "/src/images")
        
        shutil.copy(src_icon, os.path.join(self._custom_data_dir, 'src', 'icons'))
        images = os.listdir(os.path.join(os.getcwd(), 'src', 'images'))
        for img in images:
            shutil.copy(os.path.join(os.getcwd(), 'src', 'images', img), os.path.join(self._custom_data_dir, 'src', 'images'))
        
        # This put the JSON file in its corresponding place.
        src_data_json = os.path.join(os.getcwd(), 'src', 'data_actions.json')
        dst_data_json = os.path.join(self._custom_data_dir, 'src', 'data_actions.json')
        shutil.copy(src_data_json, dst_data_json)
        
    def finalize_options(self):
        install.finalize_options(self)
        
        data_dir = os.path.join(self.prefix, "share", "stickman")
        apps_dir = os.path.join(self.prefix, "share", "applications")
        pixmaps_dir = os.path.join(self.prefix, "share", "pixmaps")
        
        # if we have 'root', put the building path also under it (used normally
        # by pbuilder)
        if self.root is None:
            build_dir = data_dir
        else:
            build_dir = os.path.join(self.root, data_dir[1:])
            apps_dir = os.path.join(self.root, apps_dir[1:])
            apport_dir = os.path.join(self.root, apport_dir[1:])

        self.install_lib = build_dir
        self._custom_data_dir = data_dir
        self._custom_apps_dir = apps_dir
        if not os.path.exists(self._custom_apps_dir):
            os.makedirs(self._custom_apps_dir)
        self._custom_icon_dir = pixmaps_dir

LONG_DESCRIPTION=""" 
StickMan is a free and open software developed in Python and GTK.
It shows a toon walking, running and doing other actions on your desktop.
Still this in development."""

setup(name="StickMan",
    version="0.1",
    author="Andrés Segovia",
    author_email="andy.dev536@gmail.com"
    description="A little toon that moves on your desktop",
    long_description=LONG_DESCRIPTION,
    url="https://andy-thor.github.io/StickMan",
    license="GPLv3",
    platforms=["Linux"],
    packages=["stickman"],
    package_data={
        "src": ["icons/*", "images/stickman-*.png", "data_actions.json", "stickman.desktop"],
    },
    scripts=["stickman.py"],
    cmdclass={'install': CustomInstall,},
)
