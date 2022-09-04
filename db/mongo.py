import pymongo
import json
from random import randint
from datetime import datetime
from schemas import Struct, AlarmUpdate
from func import play_sound
import db
from bson.objectid import ObjectId
import colorlog
import logging
import multiprocessing
# mydict = {"title": "vasya", "text": "jsnfjnskajfnksjnfksnfksnjkfsd", "cases": []}
# coll.insert_one(mydict)
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
	'%(log_color)s%(levelname)s:%(name)s:%(message)s'))

logger = colorlog.getLogger('__mongo__')
logger.addHandler(handler)
logger.setLevel(logging.INFO)
def CheckAlarm():
    while True:
        if datetime.now().strftime('%S') == '30':
            data = db.coll.find_one({"date_alarm": datetime.now().strftime('%Y-%m-%d'), "time_alarm": datetime.now().strftime('%H:%M'), "status": "on"})
            if data:
                logger.info('Check alarm')
                db.coll.update_one({'_id': data['_id']}, {'$set': {"status": "off"}})
                del data['_id']
                del data['status']
                play_sound(data['song_path'])



    #RandQuestionOut(**question)

async def SetNewAlarm(data: AlarmUpdate):
    logger.info('Set new alarm')
    if not db.coll.find_one(data.dict()):
        db.coll.insert_one(data.dict())
    return data

async def Update_alarm(alarm_data: AlarmUpdate):
    logger.info('Update alarm')
    alarm_data = alarm_data.dict()
    alarm_data = {k: v for k, v in alarm_data.items() if v}
    id = alarm_data["id"]
    del alarm_data['id']
    db.coll.update_one({'_id': ObjectId(id)}, {'$set': alarm_data})
    return {"sucessful"}
async def SearchAll():
    logger.info('Search all')
    mas = db.coll.find()
    out = []
    for i in mas:
        id = i['_id']
        i['id'] = str(id)
        del i['_id']
        out.append(i)
    return out
