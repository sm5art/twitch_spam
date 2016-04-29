from pymongo import MongoClient
import pymongo

links = None
emotes = None

def init_db():
    global links
    global emotes
    client = MongoClient()
    db = client.spam_db
    links = db.links
    emotes = db.emotes
    clear_db()

def log_link(channel,message,kps,timestamp):
    if links.find_one({"message":message,"channel":channel}):
        emotes.update_one({"message":message,"channel":channel},{"$set":{"count":kps,"timestamp":timestamp}})
    else:
        links.insert_one({"message":message,"channel":channel,"count":kps,"timestamp":timestamp})
	
		
def get_last_timestamp(channel,message):
    if links.find_one({"message":message,"channel":channel}):
        return links.find_one({"message":message,"channel":channel})["timestamp"],links.find_one({"message":message,"channel":channel})["count"]
    elif emotes.find_one({"message":message,"channel":channel}):
        return emotes.find_one({"message":message,"channel":channel})["timestamp"],emotes.find_one({"message":message,"channel":channel})["count"]
    else:
        return 0,0
        
		
def log_emote(channel,message,kps,timestamp):
    if emotes.find_one({"message":message,"channel":channel}):
        emotes.update_one({"message":message,"channel":channel},{"$set":{"count":kps,"timestamp":timestamp}})
    else:
        emotes.insert_one({"message":message,"channel":channel,"count":kps,"timestamp":timestamp})

def clear_db():
    links.drop()
    emotes.drop()
    




