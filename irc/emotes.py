import json
import requests

initiated = False
emotes = []


def init_emotes():
	global initiated
	global emotes
	if not initiated:
		initiated = True
		wowzer=[]
		url = "https://twitchemotes.com/api_cache/v2/global.json"
		wow=json.loads(requests.get(url).content)["emotes"]
		for key, value  in wow.iteritems():
				wowzer.append(key)

		emotes = wowzer

