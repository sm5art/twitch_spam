import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from irc.tirc import TChannel
import requests
import re
import irc.emotes
import json


def on_message(self,message):
	for c in self.channel:
		if c.encode('ascii', 'ignore') in message:
			channel = c


		
	for x in irc.emotes.emotes:
		if x in message:
			element = {"channel":channel,"message":x}
			print element
			self.buffer.push(element)
			break
		
	link_factory = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", message)
	if len(link_factory)>0:
			element = {"channel":channel,"message":link_factory[0]}
			self.buffer.push(element)
			print element

twitch = requests.get("https://api.twitch.tv/kraken/streams")
channel = json.loads(twitch.content)

 
TChannel(on_message,channel = [channel["streams"][i]["channel"]["name"] for i in range(0,20)])
TChannel(on_message,channel = [channel["streams"][i]["channel"]["name"] for i in range(20,40)])
TChannel(on_message,channel = [channel["streams"][i]["channel"]["name"] for i in range(40,60)])
TChannel(on_message,channel = [channel["streams"][i]["channel"]["name"] for i in range(60,80)])





