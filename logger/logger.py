import json
class JSON_queue(object): #ooh trendy 
    def __init__(self, json_file):
        self.queued = 0
        self.queue = []
        self.json = json_file
    def loglink(self, link):
        self.queue.append(link)
    def add_next(self):
        link = self.queue.pop(0) #get first added item
        formatted_link = link.lower()
        try:
            links = dict(self.load())
        except Exception:
            links = {}
        if link in links.keys():
            links[formatted_link] += 1
        else:
            links[formatted_link] = 1
        self.save(links)
    def save(self, data):  
        with open(self.json, 'wb') as outfile:
            json.dump(data, outfile)
    def load(self):
        with open(self.json) as infile:
            data = json.load(infile)
        return data
    def clear(self):
        with open(self.json, 'wb') as outfile:
            json.dump({}, outfile)
