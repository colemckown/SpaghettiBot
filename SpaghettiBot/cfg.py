#cfg.py

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

"""import os

# change directory to CONFIG file -- normalized for better crossplatform-ability
os.chdir(os.path.join(os.path.abspath(__file__), os.path.normpath("/dist/CONFIG/")))
"""
import os
import shutil

shutil.rmtree(os.path.abspath("CONFIG"), True)
shutil.copytree(os.path.abspath("../../CONFIG"), os.path.abspath("CONFIG"))

os.chdir(os.path.abspath("CONFIG"))
print("{}{}".format("Reading configuration files from ", os.path.abspath(os.curdir)))

s = open("systemconfig.txt", "r")
systemSettings = s.readlines()
s.close()

for line in systemSettings:
	if line.startswith("$"):
		setting = systemSettings[systemSettings.index(line) + 1].rstrip("\n")
		if line.startswith("$HOST"):
			HOST = setting
		elif line.startswith("$PORT"):
			PORT = int(setting)
		elif line.startswith("$NICK"):
			NICK = setting
		elif line.startswith("$PASS"):
			PASS = setting
		elif line.startswith("$CHAN"):
			CHAN = setting
		elif line.startswith("$RATE"):
			RATE = float(setting)

m = open("messageconfig.txt", "r")
messages = m.readlines()
m.close()

for line in messages:
	if line.startswith("$"):
		message = messages[messages.index(line) + 1].rstrip("\n")
		# god save us all
		if line.startswith("$DISC"):
			DISC = message
		elif line.startswith("$DISM"):
			DISM = message
		elif line.startswith("$NTPR"):
			NTPR = message
		elif line.startswith("$QUEF"):
			QUEF = message
		elif line.startswith("$QEMP"):
			QEMP = message
		elif line.startswith("$GGTX"):
			GGTX = message
		elif line.startswith("$QNXT"):
			QNXT = message
		elif line.startswith("$PTNC"):
			PTNC = message
		elif line.startswith("$ADDM"):
			ADDM = message
		elif line.startswith("$POS1"):
			POS1 = message
		elif line.startswith("$POS2"):
			POS2 = message
		elif line.startswith("$NOTQ"):
			NOTQ = message
		elif line.startswith("$WHMS"):
			WHMS = message
		elif line.startswith("$NOCH"):
			NOCH = message
		elif line.startswith("$HELP"):
			HELP = message
		elif line.startswith("$LEFT"):
			LEFT = message
		elif line.startswith("$QCLR"):
			QCLR = message
		elif line.startswith("$WHNX"):
			WHNX = message
		elif line.startswith("$QTOT"):
			QTOT = message
		elif line.startswith("$QEMP"):
			QEMP = message

MODS = []
PATT = []
COMM = []
MDCM = []
MESS = []

l = open("listconfig.txt", "r")
lists = l.readlines()
l.close()

for line in lists:
	lists[lists.index(line)] = lists[lists.index(line)].rstrip()

for line in lists:
	if line.startswith("$"):
		if line.startswith("$MODS"):
			for mod in range(lists.index(line) + 1, lists.index("$ENDMODS")):
				MODS.append(lists[mod])
		elif line.startswith("$PATT"):
			for pattern in range(lists.index(line) + 1, lists.index("$ENDPATT")):
				PATT.append(lists[pattern])
		elif line.startswith("$COMM"):
			for command in range(lists.index(line) + 1, lists.index("$ENDCOMM")):
				COMM.append(lists[command])
		elif line.startswith("$MDCM"):
			for modcomm in range(lists.index(line) + 1, lists.index("$ENDMDCM")):
				MDCM.append(lists[modcomm])
		elif line.startswith("$MESS"):
			for message in range(lists.index(line) + 1, lists.index("$ENDMESS")):
				MESS.append(lists[message])
