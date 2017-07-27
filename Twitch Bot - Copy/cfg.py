# cfg.py
HOST = "irc.twitch.tv"              			# the Twitch IRC server
PORT = 6667                         			# always use port 6667!
NICK = "bot_nickname"            				# your Twitch username, lowercase
PASS = "oauth:xxxxxxxxxxxxxxxxxxxxxxxxxxxx" 	# your Twitch OAuth token
CHAN = "#channel"                 				# the channel you want to join
RATE = (20.0/30.0)								# messages per second


DISC = "https://discord.gg/xxxx"				# discord link
DISM = "Discord: "								# first part of message before discord link
NTPR = "That command isn't for you, "			# message displayed when someone tries to execute a command that they shouldn't be
QUEF = "queue.txt"								# filename for queue text file
QEMP = "The queue is empty."					# message displayed when queueNext() is called and queue is empty
GGTX = "GG's, "									# message displayed when done with current challenger (ends with "<username>")
QNXT = " is next up."							# message displayed when next in queue is ready (starts with "<username>")
PTNC = " is already in queue. Be patient!"		# message when trying to enter queue while already in (starts with "<user>")
ADDM = " has been added to the queue!"			# message when user successfully added to queue
POS1 = " challengers are ahead of "				# message to show user's position in queue (starts with "<number in front of user>")
POS2 = " in queue."								# finishes above (after "<username>")
NOTQ = " is not in queue."						# message to show when user checks position in queue but is not in queue (starts with "<user>")
WHMS = "<name> is playing with "				# message to show current challenger (before "<challenger>")
NOCH = "<name> doesn't have a challenger yet. Type !play to be the first."
HELP = "Go to https://pastebin.com/0LrYJCJS to see list of commands."									# message to link to list of commands
LEFT = " has left the queue."					# message to show when user leaves queue (starts with "<username>")

PATT = [
	]											# ban patterns
COMM = ["!check", "!imgay", "!discord", "!play", "!next", "!position", "!who", "!help", "!cancel"
	]											# commands
MESS = [
    ]											# messages to be sent periodically with every PING
