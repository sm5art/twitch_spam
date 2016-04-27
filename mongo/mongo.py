from pymongo import MongoClient


client = MongoClient()
db = client.spam_db
links = db.links
emotes = db.emotes

def log_link(link):
	if links.find_one({"link":link}):
		#unfinished



