import string
import time
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom

s = openSocket()
startTime = time.time()
joinRoom(s)
readbuffer = ""

while True:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()

		for line in temp:
			print(line)
			if "PING" in line:
				s.send(line.replace("PING", "PONG"))
				break
			user = getUser(line)
			message = getMessage(line)
			print user + " typed :" + message
			if "asdf" in message:
				sendMessage(s, "ghjkl")
				break
			if "uptime" in message:


				sendMessage(s, "")
				break
			if "DansGame" in message:
				sendMessage(s, "http://i.imgur.com/XCnQzbL.png")
				break
			if "useless" in message:
				sendMessage(s, "i know, im a useless bot FeelsBadMan")
				break
			if "!ding" in message:
				sendMessage(s, "weebs (puke)")
				break
			if "!vanish" in message:
				sendMessage(s, user + " just vanished! haha exposed lolol xD :tf:")
				break
			if "get spooked" in message:
				sendMessage(s, "http://th0mk.github.io/paja/")
				break
			if "secretquitcode123" in message:
				sendMessage(s, "bye :tf:")
				break
			if "secretquitcode321" in message:
				sendMessage(s, "STOP QUITTING ME DansGame")
				exit()
				break
