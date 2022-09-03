from pydantic import BaseModel, validator
from datetime import datetime, date, timedelta
import re
import logging
import colorlog
class Struct(BaseModel):
    song_path: str = 'claymore_ringtone'
    date_alarm: str = datetime.now().strftime('%Y-%m-%d')
    time_alarm: str = datetime.now().strftime("%H:%M")
    status: str = 'on'
    @validator("date_alarm", pre=True)
    def parse_date(cls, value):
        tpl = '2022-[0-1][0-9]-[0-3][0-9]$'
        if re.match(tpl, value):
            return value
        else:
            raise ValueError("Invalid Date")

    @validator("time_alarm", pre=True)
    def parse_time(cls, value):
        tpl = '[0-2][0-9]:[0-5][0-9]$'
        if re.match(tpl, value):
            return value
        else:
            raise ValueError("Invalid Time")
class AlarmUpdate(BaseModel):
    id: str
    song_name: str = 'claymore_ringtone'
    date_alarm: str = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    time_alarm: str = datetime.now().strftime("%H:%M")
    status: str = 'on'

    @validator("date_alarm", pre=True)
    def parse_date(cls, value):
        tpl = '2022-[0-1][0-9]-[0-3][0-9]$'
        if re.match(tpl, value):
            return value
        else:
            raise ValueError("Invalid Date")

    @validator("time_alarm", pre=True)
    def parse_time(cls, value):
        tpl = '[0-2][0-9]:[0-5][0-9]$'
        if re.match(tpl, value):
            return value
        else:
            raise ValueError("Invalid Time")

