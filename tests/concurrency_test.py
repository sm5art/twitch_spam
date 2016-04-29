import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from irc.tirc import TChannel
import requests
import re
import irc.emotes
import json
import mongo.mongo as mongo
import time

mongo.init_db()

time_log = {}

def on_message(self,message):
    global time_log
    global time_start
    if time.time() - time_start > 30:
        time_start= time.time()
        time_log = {}
    for c in self.channel:
		if c.encode('ascii', 'ignore') in message:
			channel = c

    
    for x in irc.emotes.emotes:
		if x in message:
		    element = {"channel":channel,"message":x}
		    if channel in time_log and x in time_log[channel]:
		        time_log[channel][x] = time_log[channel][x]+1
		    else:
		        time_log[channel]={x:1}
		    
		    current_time = time.time()
		    avg = (current_time-time_start)
		    kps = int(time_log[channel][x]/(avg)*60)
		    if kps >0:
		        print kps, element
		    mongo.log_emote(channel,x,kps,current_time)
		    self.buffer.push(element)
		  
		    break
"""		
    link_factory = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", message)
    if len(link_factory)>0:
        x=link_factory[0]
        element = {"channel":channel,"message":x}
        if channel in channel_count and x in channel_count[channel]:
            channel_count[channel][x]["count"]+=1
        else:
		    channel_count[channel]={x:{"count":0}}
        if channel_count[channel][x]["count"] % 5 == 0:
		    current_time = time.time()
		    last_timestamp,last_kps = mongo.get_last_timestamp(channel,x)
		    kps = int(5/(current_time-last_timestamp)*60)
		    mongo.log_emote(channel,x,kps,current_time)
		    print element
		    self.buffer.push(element)
		    channel_count[channel][x]["count"] = 0
		    """

twitch = requests.get("https://api.twitch.tv/kraken/streams")
channel = json.loads(twitch.content)

 
TChannel(on_message,channel = [channel["streams"][i]["channel"]["name"] for i in range(0,20)])
time_start= time.time()




