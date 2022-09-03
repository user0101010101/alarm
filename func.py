import os
from os import path
import datetime
import multiprocessing
import re
import time
import logging
from playsound import playsound
import logging
import colorlog

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
	'%(log_color)s%(levelname)s:%(name)s:%(message)s'))

logger = colorlog.getLogger('__func__')
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def play_sound(name_sound):
    logger.info('Play sound')
    for p in multiprocessing.active_children():
        if p.name == "playing":
            p.terminate()
    parent_dir = path.dirname(path.abspath(__file__))
    full_path = parent_dir + '/res/' + name_sound + '.mp3'
    p = multiprocessing.Process(target=playsound, args=(full_path,), name='playing')
    p.start()
    return p

def stop_sound():
    logger.info('Stop sound')
    for p in multiprocessing.active_children():
        print(p.name)
        if p.name == 'playing':
            p.terminate()

async def show_all_sounds():
    logger.info('Show all sound')
    parent_dir = path.dirname(path.abspath(__file__)) + '/res/'
    three = os.walk(parent_dir)
    out_dict = []
    for admin, dirs, files in three:
        for file in files:
            file_name = file[:(re.search('[.]', file).span()[0])]
            out_dict.append(file_name)
    return out_dict


    #user_sound_process = play_sound('/Users/levugfeld/Desktop/sounds_alarm', 'claymore_ringtone.mp3')

    #stop_sound(user_sound_process)