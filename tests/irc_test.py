import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from irc.tirc import TChannel
import requests
import json

session = requests.Session()
twitch = session.get("https://api.twitch.tv/kraken/streams")
channel = json.loads(twitch.content)
name =  channel["streams"][1]["channel"]["name"]

channel = TChannel(channel = "arturbabeav")
