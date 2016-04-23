import json
def loglink(link):
  formatted_link = link.lower()
  try:
    links = dict(load())
  except Exception:
    links = {}
  if link in links.keys():
    links[formatted_link] += 1
  else:
    links[formatted_link] = 1
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