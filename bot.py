#!/usr/bin/python
import irclib
import ircbot
import random
import re
class Bot(ircbot.SingleServerIRCBot):
	def __init__(self):
		global server
		global nick
		global realname
		global port
		print "Is going to join server "+server+" with port "+port+" on channel "+channel+" with nick "+nick+" and with real name "+realname+"."
		ircbot.SingleServerIRCBot.__init__(self, [(server, int(port))], nick, realname)
	def on_welcome(self, serv, ev):
		global channel
		serv.join(channel)
	def on_pubmsg(self, serv, ev):
		global channel
		
		# Badwords...
		global kick_messages_badword
		global kick_messages_flood
		badwords = open("badwords.txt")
		message = ev.arguments()[0]
		for line in badwords :
			if re.match("((.)* ){,1}"+line[:-1]+" (.)*", message.lower()) != None or line[:-1] in message.lower().split() or re.match("((.)* ){,1}"+line[:-1]+"\W", message.lower()) != None : # If we find the WORD in the message
				serv.kick(channel, irclib.nm_to_n(ev.source()), kick_messages_badword[random.randint(0, len(kick_messages_badword)-1)])
		badwords.close()
		
		# And flood...
		if len(message) > 350 :
			serv.kick(channel, irclib.nm_to_n(ev.source()), kick_messages_flood[random.randint(0, len(kick_messages_flood)-1)])


config = open("config.txt", "r")
# Default congiguration
port = 6667
realname = "realname"
# config.txt reading
for line in config :
	obj = line.split(':')[0]
	if obj == "channel" :
		channel = line.split(':')[1]
		if channel[len(channel)-1] == '\n' :
			channel = channel[:-1]
	elif obj == "server" :
		server = line.split(':')[1]
		if server[len(server)-1] == '\n' :
			server = server[:-1]
	elif obj == "nick" :
		nick = line.split(':')[1]
		if nick[len(nick)-1] == '\n' :
			nick = nick[:-1]
	elif obj == "realname" :
		realname = line.split(':')[1]
		if realname[len(realname)-1] == '\n' :
			realname = realname[:-1]
	elif obj == "port" :
		port = line.split(':')[1]
		if port[len(port)-1] == '\n' :
			port = port[:-1]
	else :
		print "Invalid config.txt file. Line : "+line
		config.close()
		quit()
config.close()

# Open kick_messages_badword.txt and create a list of kick messages
kick_messages_file = open("kick_messages_badword.txt", "r")
kick_messages_badword = []
for line in kick_messages_file :
	kick_messages_badword.append(line)
kick_messages_file.close()
# Open kick_messages_flood.txt and create a list of kick messages
kick_messages_file = open("kick_messages_flood.txt", "r")
kick_messages_flood = []
for line in kick_messages_file :
	kick_messages_flood.append(line)
kick_messages_file.close()
 
if __name__ == "__main__":
	Bot().start()
