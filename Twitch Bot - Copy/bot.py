# bot.py

import cfg
import os
import socket
import re
import time

# network functions go here

def chat(sock, msg):
    """
    Send a chat message to the server.
    Keyword arguments:
    sock -- the socket over which to send the message
    msg  -- the message to be sent
    """
    sock.send("PRIVMSG {} :{}\r\n".format(cfg.CHAN, msg))
    print(cfg.NICK + ": " + msg)

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
    timeout(sock, user, 10)  

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
        chat(sock, "{}{}".format(user, cfg.NOTQ))

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
        chat(s, "{}{}".format(user, cfg.LEFT))
    else:
        chat(s, "{}{}".format(user, cfg.NOTQ))

def who(sock, chall):
    if not chall == "nobody":
        chat(sock, "{}{}".format(cfg.WHMS, chall))
    else:
        chat(sock, "{}".format(cfg.NOCH))

def help(sock):
    chat(sock, "{}".format(cfg.HELP))


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


CHAT_MSG=re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

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
                elif command == "!next":
                    if username == cfg.CHAN:
                        challenger = queueNext(s, f, challenger)
                        break
                    else:
                        notPermitted(s, username)
                        break
                elif command == "!position":
                    queuePosition(s, username, f)
                    break
                elif command == "!who":
                    who(s, challenger)
                    break
                elif command == "!help":
                    help(s)
                    break
                elif command == "!cancel":
                    queueLeave(s, username, f)
                    break


    time.sleep(1.0 / cfg.RATE)
