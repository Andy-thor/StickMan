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

from stickman.main import main
from gi.repository import Gtk
import sys
import gi
gi.require_version('Gtk', '3.0')


def show_license():
    print(
        "Copyright (C) 2019  Andrés Segovia\n"
        "This program comes with ABSOLUTELY NO WARRANTY. This is free software, and\n"
        "you are welcome to redistribute it under certain conditions. See the GNU\n"
        "General Public License for details.\n"
    )


def version():
    print("StickMan 0.1\n")


def usage():
    print(
        "{}: stickman [OPTION]\n"
        "{}\n\n"
        "{}:\n"
        " -h, --help\t\t{}\n"
        " -v, --version\t\t{}\n"
        " -l, --license\t\t{}\n"
        " -r, --run-local\t{}\n".format(
            "Usage",
            "Show a toon in your desktop",
            "Options",
            "Display this message and exit.",
            "Print version information.",
            "Show the type of license of this software",
            "Run locally from source code only"))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        if arg in ('-h', '--help'):
            usage()
            sys.exit()
        elif arg in ('-v', '--version'):
            version()
            sys.exit()
        elif arg in ('-l', '--license'):
            show_license()
            sys.exit()
        elif arg in ('-r', '--run-local'):
            gui = main(run_local=True)
            Gtk.main()
        else:
            print("Incorrect option")
            print("Try \"--help\" to see a list of available command line options")
            sys.exit()
    else:
        gui = main()
        Gtk.main()
