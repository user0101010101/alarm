from fastapi import FastAPI, Query, Path, Body
from datetime import datetime
import uvicorn
from schemas import Struct, AlarmUpdate
from db.mongo import SetNewAlarm, CheckAlarm, Update_alarm, SearchAll
from typing import List
from func import play_sound, stop_sound, show_all_sounds
import multiprocessing
import logging
import colorlog
app = FastAPI()

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
	'%(log_color)s%(levelname)s:%(name)s:%(message)s'))

logger = colorlog.getLogger('__main__')
logger.addHandler(handler)
logger.setLevel(logging.INFO)

logger.info("Checker started")
process_checker = multiprocessing.Process(target=CheckAlarm, name='checker')
process_checker.start()
@app.get('/')
async def hello_user():
    logger.info('Hello')

    return {"Hello user"}



@app.post("/set_alarm", response_model=Struct)
async def set_alarm(item: Struct):
    logger.info('Set alarm')
    return await SetNewAlarm(item)

@app.get('/stop')
async def stop_alarm():
    logger.info('Stop sound')
    return stop_sound()
@app.post('/reload_alarm')
async def reload_alarm(alarm_data: AlarmUpdate):
    logger.info('Reload alarm')
    return await Update_alarm(alarm_data)
@app.get('/all_alarms')
async def show_all_alarms():
    logger.info('Show all alarms')
    return await SearchAll()
@app.get('/show_all_sounds')
async def get_all_sounds():
    logger.info('Show all sounds')
    return await show_all_sounds()
#https://github.com/pybluez/pybluez.git