import socket
from random import randint


class TChannel():
	def __init__(self, channel = "",buffer=100):
		self.host = "irc.chat.twitch.tv"
		self.port = 6667
		self.buffer = MessageBuffer(buffer)
		self.nick = "justinfan"+"".join("%s" % randint(0,9) for i in range(0,10))
		self.PASS = "doesnotmatter"
		self.channel = channel
		s=socket.socket( )
		s.connect((self.host, self.port))
		s.send("PASS %s\r\n" % self.PASS)
		s.send("NICK %s\r\n" % self.nick)
		self.join(s)

	def join(self,s):
		s.send("JOIN #%s\r\n" % self.channel)
		self.populatebuffer(s)

	def populatebuffer(self,s):
		while 1:
			message = s.recv(1024)
			self.on_message(message)

	def on_message(self,message):
		self.buffer.push(message)
		print message



class MessageBuffer():
	def __init__(self,size):
		self.buffer_content = []
		self.size = size

	def push(self,message):
		if len(self.buffer_content) >= self.size:
			self.buffer.remove(0)
			self.buffer_content.append(message)
		else:
			self.buffer_content.append(message)

	def __str__(self):
		return self.buffer[len(self.buffer)-1]
