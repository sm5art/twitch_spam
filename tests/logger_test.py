import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from logger.logger import JSON_queue

queue = JSON_queue('links.json')
queue.clear() #test clear()
assert queue.load() == {} 
test_link = "www.whatthes.net"
queue.loglink(test_link) #test loglink()
queue.add_next()
assert queue.load()[test_link] == 1
queue.load()
queue.load() #test consecutive load calls
assert queue.load()[test_link] == 1 
temp = queue.load()
queue.save(queue.load())
assert queue.load() == temp #sanity check
queue.loglink(test_link.upper())
queue.add_next()
assert queue.load()[test_link] == 1 #check capitalization
queue.clear() #clean up
