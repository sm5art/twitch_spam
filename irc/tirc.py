import socket
import threading
import json
import re
from random import randint


class TChannel(threading.Thread):
	def __init__(self, channel = "",length=50):
		super(TChannel, self).__init__()
		self.host = "irc.chat.twitch.tv"
		self.port = 6667
		self.buffer = MessageBuffer(length)
		self.nick = "justinfan"+"".join("%s" % randint(0,9) for i in range(0,10))
		self.PASS = "doesnotmatter"
		self.channel = channel
		self.start()
		self.join()

	def run(self):
		s=socket.socket( )
		s.connect((self.host, self.port))
		s.send("PASS %s\r\n" % self.PASS)
		s.send("NICK %s\r\n" % self.nick)
		self.join_channel(s)

	def join_channel(self,s):
		s.send("JOIN #%s\r\n" % self.channel)
		self.populate_buffer(s)

	def populate_buffer(self,s):
		while 1:
			message = s.recv(1024)
			self.on_message(message)

	def on_message(self,message):
		
		#if "#" in message and "!" in message:
		   #message = message[1:message.index("!")] + message[message.index("#"):]
		message = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", message)
		if len(message)>0:
				print message[0]
				self.buffer.push(message[0])



class MessageBuffer():
	def __init__(self,size):
		self.buffer_content = []
		self.size = size

	def push(self,message):
		if len(self.buffer_content) >= self.size:
			self.buffer_content.pop(0)
			self.buffer_content.append(message)
		else:
			self.buffer_content.append(message)

	def __str__(self):
		return json.dumps({"buffer":self.buffer_content})
