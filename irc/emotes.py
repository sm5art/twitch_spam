import json
import requests

initiated = False
emotes = []


def init_emotes():
	initiated = True
	wowzer=[]
	url = "https://twitchemotes.com/api_cache/v2/global.json"
	wow=json.loads(requests.get(url).content)["emotes"]
	for key, value  in wow.iteritems():
		wowzer.append(key)

	return wowzer


if __name__ == "__main__":
	emotes = init_emotes()