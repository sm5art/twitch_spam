import json
def loglink(link):
  try:
    links = dict(load())
  except Exception:
    links = {}
  if link in links.keys():
    links[link] += 1
  else:
    links[link] = 1
  save(links)
def save(data):  
  with open('links.json', 'wb') as outfile:
    json.dump(data, outfile)
def load():
  with open('links.json') as infile:
    data = json.load(infile)
  return data
def clear():
  with open('links.json', 'wb') as outfile:
    json.dump({}, outfile)