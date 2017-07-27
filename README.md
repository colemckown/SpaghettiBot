# SpaghettiBot
A socket based Twitch bot written in Python; an eternal work in progress

Repository: github.com/colemckown/spaghettibot


CONFIGURATION:

User end configuration is done through editing the files: systemconfig.txt, messageconfig.txt, and listconfig.txt

GLOBAL RULES FOR CONFIGURATION:

	1. MAINTAIN THE FORMAT
	2. See rule 1


FILE SPECEFIC RULES FOR CONFIGURATION:

----------------------------------------------------------------
	systemconfig.txt:
	
	Don't add or remove any settings from this list. Make sure all letters in the settings are lower-case
	If you modify a setting, be sure to maintain the format by including the value of the setting (and nothing else) in the line immediately after the delineator for the setting (eg $HOST). 

	Configuration of this file is entirely necessary to be able to run the bot.
	The $HOST and $PORT should not be changed (assuming you are connecting the bot to Twitch)
	$NICK should be the username of the bot's Twitch account
	$CHAN should be the username of the streamer to whose channel you want the bot to connect.
		***NOTE: LEAVE THE '#' PRECEDING THE CHANNEL NAME***
	$RATE can stay at its default. The default will limit the bot's rate of sending/receiving messages to the maximum allowed before the Twitch IRC server will ban the user, (20 messages per 30 seconds) so be weary of this if you intend to change this for whatever reason. It also serves as CPU optimization.
----------------------------------------------------------------


----------------------------------------------------------------
	messageconfig.txt:

	This should be the least sensitive of the config files.
	Still be sure to maintain the format by including the entire message in one line immediately after its respective delineator.

	Be mindful of how your message will appear in practice, and how you should manage spacing accordingly.
	For example: If you want the !discord command to look like "Discord: <link>" the $DISM will need to have the colon and the space or else it will be "Discord<link>" when messaged
----------------------------------------------------------------

----------------------------------------------------------------
	listconfig.txt

	Format is more important in this one than ever. Maintain it.
	Make sure each element of each list has its own line in its entirety and that there is nothing else on that line.
	Make sure each list is enclosed with a preceding delineator (eg $LIST) and a trailing delineator (eg $ENDLIST) with no whitespace in between.
----------------------------------------------------------------