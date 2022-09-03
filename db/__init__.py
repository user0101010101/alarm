import pymongo
import colorlog
import logging
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
	'%(log_color)s%(levelname)s:%(name)s:%(message)s'))

logger = colorlog.getLogger('__mongo_init__')
logger.addHandler(handler)
logger.setLevel(logging.INFO)

logger.info('Connect mongo')
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.Alarm
coll = db['list_alarms']
# mydict = {"path": "fjhnabwkfnlijwnfw"}
# coll.insert_one(mydict)