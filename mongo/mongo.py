from pymongo import MongoClient


client = MongoClient()
db = client.spam_db
links = db.links
emotes = db.emotes

def log_link(channel,message):
    if links.find_one({"message":message,"channel":channel}):
        links.update_one({"message":message,"channel":channel},{"$inc":{"count":1}})
    else:
        links.insert_one({"message":message,"channel":channel,"count":1})
	
		
		
def log_emote(channel,message):
    if emotes.find_one({"message":message,"channel":channel}):
        emotes.update_one({"message":message,"channel":channel},{"$inc":{"count":1}})
    else:
        emotes.insert_one({"message":message,"channel":channel,"count":1})



