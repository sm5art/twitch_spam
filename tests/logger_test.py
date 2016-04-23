import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import logger.logger

logger.clear() #test clear()
assert logger.load() == {} 
test_link = "www.whatthes.net"
logger.loglink(test_link) #test loglink()
assert logger.load()[test_link] == 1
logger.load()
logger.load() #test consecutive load calls
assert logger.load()[test_link] == 1 
temp = logger.load()
logger.save(logger.load())
assert logger.load() == temp #sanity check
logger.loglink(test_link.upper())
assert logger.load()[test_link] == 1 #check capitalization
logger.clear() #clean up
