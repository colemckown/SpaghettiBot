# bot.py

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

import os
import cfg
import socket
import re
import time
import sys

# network functions go here

def chat(sock, msg):
    """
    Send a chat message to the server.
    Keyword arguments:
    sock -- the socket over which to send the message
    msg  -- the message to be sent
    """
    sock.send("PRIVMSG {} :{}\r\n".format(cfg.CHAN, msg))
    print("\n" + cfg.NICK + ": " + msg + "\n")

def ban(sock, user):
    """
    Ban a user from the current channel.
    Keyword arguments:
    sock -- the socket over which to send the ban command
    user -- the user to be banned
    """
    chat(sock, ".ban {}".format(user))

def timeout(sock, user, secs=600):
    """
    Time out a user for a set period of time.
    Keyword arguments:
    sock -- the socket over which to send the timeout command
    user -- the user to be timed out
    secs -- the length of the timeout in seconds (default 600)
    """
    chat(sock, ".timeout {}".format(user, secs))


# checks to see if the bot is alive
def check(sock):
    chat(sock, "{} is up and running!".format(cfg.NICK))

# tells everyone that you're gay (hopefully they won't notice though)
def imgay(sock, user):
    chat(sock, "The chat is moving so fast that no one will notice {} is gay 4Head".format(user))

# displays link to discord channel
def discord(sock):
    chat(sock, "{}{}".format(cfg.DISM, cfg.DISC))  

# slaps people on the wrist when they try to do things they're not allowed to do
def notPermitted(sock, user):
    chat(sock, "{}{}".format(cfg.NTPR, user)) 

# sends a list of messages (defined in cfg.MESS) to be sent upon every IRC server PING/PONG
def periodicMessage(sock, counter):
    chat(sock, cfg.MESS[counter])

# adds user to queue
def queueAdd(sock, user, file):
    if user in open(file).read():
        chat(sock, "{}{}".format(user, cfg.PTNC))
    else:
        chat(sock, "{}{}".format(user, cfg.ADDM))
        with open(file, "a") as f:
            f.write("{}\n".format(user))

# finishes session with current challenger and starts a new one with next in queue
def queueNext(sock, file, chall):
    if not chall == "nobody":
        chat(sock, "{}{}".format(cfg.GGTX, chall))
    if os.path.getsize(file) == 0:
        chat(sock, cfg.QEMP)
        return "nobody"
    else:
        f = open(file, "r")
        userList = f.readlines()
        f.close()
        c = userList[0].rstrip()
        chat(sock, "{}{}".format(c, cfg.QNXT))
        del userList[0]
        f = open(file, "w")
        f.writelines(userList)
        f.close()
        return c

# checks the position of a user in the queue
def queuePosition(sock, user, file):
    f = open(file, "r")
    userList = f.readlines()
    f.close()
    for u in userList:
        userList[userList.index(u)] = userList[userList.index(u)].rstrip()
    if user in userList:
        chat(sock, "{}{}{}{}".format(userList.index(user), cfg.POS1, user, cfg.POS2))
    else:
        notInQueue(sock, user)

def queueLeave(sock, user, file):
    f = open(file, "r")
    userList = f.readlines()
    f.close()

    for u in userList:
        userList[userList.index(u)] = userList[userList.index(u)].rstrip()
    if user in userList:
        del userList[userList.index(user)]
        for u in userList:
            userList[userList.index(u)] = "{}\n".format(userList[userList.index(u)])
        f = open(file, "w")
        f.writelines(userList)
        f.close()
        chat(sock, "{}{}".format(user, cfg.LEFT))
    else:
        notInQueue(sock, user)

def queueClear(sock, file):
    open(file, "w").close()
    chat(sock, "{}".format(cfg.QCLR))
    return "nobody"

def noChallengers(sock):
    chat(sock, "{}".format(cfg.NOCH))

def queueEmpty(sock):
    chat(sock, "{}".format(cfg.QEMP))

def notInQueue(sock, user):
    chat(sock, "{}{}".format(user, cfg.NOTQ))

def who(sock, chall):
    if not chall == "nobody":
        chat(sock, "{}{}".format(cfg.WHMS, chall))
    else:
        noChallengers(sock)

def whonext(sock, file):
    f = open(file, "r")
    userList = f.readlines()
    f.close()
    if not len(userList) == 0:
        chat(sock, "{}{}".format(userList[0].rstrip(), cfg.WHNX))
    else:
        queueEmpty(sock)

def total(sock, file):
    f = open(file, "r")
    userList = f.readlines()
    f.close()
    if len(userList) > 0:
        chat(sock, "{}{}".format(len(userList), cfg.QTOT))
    else:
        queueEmpty(sock)

def bracket(sock):
	chat("{}{}".format(cfg.BRMS, cfg.BRCK))

def help(sock):
    chat(sock, "{}".format(cfg.HELP))

def kill(sock):
	chat(sock, "{}{}".format(cfg.NICK, cfg.KILL))
	sys.exit()

# ugly system/networking stuff... there has to be a better way to do this but idk man

# connect to server
s = socket.socket()
s.connect((cfg.HOST, cfg.PORT))
s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(cfg.CHAN).encode("utf-8"))

chat(s, "{} is starting up.".format(cfg.NICK))

f = cfg.QUEF
open(f, "w").close()

challenger = "nobody"
messageCounter = 0
CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")


while True:
    response = s.recv(4096).decode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        periodicMessage(s, messageCounter)
        if messageCounter == len(cfg.MESS) - 1:
            messageCounter = 0
        else:
            messageCounter += 1
    else:
        username = re.search(r"\w+", response).group(0) # return the entire match
        message = CHAT_MSG.sub("", response)
        print(username + ": " + message)
        
        for pattern in cfg.PATT:
            if re.match(pattern, message):
                timeout(s, username)
                break
        for command in cfg.COMM:
            if message.startswith(command):
                if command == "!check":
                    check(s)
                    break
                elif command == "!imgay":
                    imgay(s, username)
                    break
                elif command == "!discord":
                    discord(s)
                    break
                elif command == "!play":
                    queueAdd(s, username, f)
                    break
                elif command == "!position":
                    queuePosition(s, username, f)
                    break
                elif command == "!who":
                    who(s, challenger)
                    break
                elif command == "!whonext":
                    whonext(s, f)
                    break
                elif command == "!help":
                    help(s)
                    break
                elif command == "!cancel":
                    queueLeave(s, username, f)
                    break
                elif command == "!total":
                    total(s, f)
                    break
                elif command == "!bracket":
                	bracket(s)
                	break
        for command in cfg.MDCM:
            if message.startswith(command):
                if username in cfg.MODS:
                    if command == "!next":
                        challenger = queueNext(s, f, challenger)
                        break
                    elif command == "!clear":
                        challenger = queueClear(s, f)
                        break
                    elif command == "!kill":
                    	kill(s)
                    	break
                else:
                    notPermitted(s, username)
                    break

    time.sleep(1.0 / cfg.RATE)
