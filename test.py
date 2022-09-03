import time
import threading
from datetime import datetime, timedelta
import db
from bson.objectid import ObjectId
from os import path
import logging
import multiprocessing

import bluetooth
from playsound import playsound





if __name__ == '__main__':

    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("Found {} devices.".format(len(nearby_devices)))

    for addr, name in nearby_devices:
        print("  {} - {}".format(addr, name))

    # full_path = '/Users/levugfeld/PycharmProjects/Alarm/res/claymore_ringtone.mp3'
    # p = multiprocessing.Process(target=playsound, args=(full_path,), name='playing')
    # p.start()
    # time.sleep(5)
    # for p in multiprocessing.active_children():
    #     print(p.name)

# times = ['00:12']
# thread = threading.Thread(target=checker, args=[times])
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger('Log')
# logger.info('fdsfsd')
# parent_dir = path.dirname(path.abspath(__file__))
# print(type(parent_dir))
#thread.start()

#print( (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d') )

#print(db.coll.find_one({'_id' : ObjectId('630f93bf56406053156f3b46')}))
#db.coll.update_one({'_id' : ObjectId('630f93bf56406053156f3b46')}, {'$set': {'status': 'on'}})