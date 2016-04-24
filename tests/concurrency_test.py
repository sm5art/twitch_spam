import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from irc.tirc import TChannel
import requests
import json



twitch = requests.get("https://api.twitch.tv/kraken/streams")
channel = json.loads(twitch.content)

for i in range(0,50):
	TChannel(channel = channel["streams"][i]["channel"]["name"])





