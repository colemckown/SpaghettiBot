# setup.py

### Copyright 2017 Cole McKown

"""
    This file is part of SpaghettiBot.

    SpaghettiBot is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    SpaghettiBot is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Spaghettibot.  If not, see <http://www.gnu.org/licenses/>.
"""

from distutils.core import setup
import py2exe

setup(console=["bot.py"])