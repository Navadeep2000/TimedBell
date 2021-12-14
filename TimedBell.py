# School bell
from pygame import mixer
import datetime as dt
import time
import re


def Bell_Time(input_time):  # Input time is fed to this function
    Bell_Time_schedule = ['09:30:00', '11:10:00', '13:00:00', '16:00:00']
    # All different time periods when the bell has to ring
    if input_time in Bell_Time_schedule:
        return 'Bell'


mixer.init()
mixer.music.load("bell.mp3")
while True:
    Time = str(dt.datetime.now())
    # Records current time, date, seconds & converting obtained value to string

    res_time = re.findall(r"\d{1,2}[:]\d{2}[:]\d{2}", Time)
    # To Record the current time in HH : MM format, we use regular expression

    print(res_time[0])

    if Bell_Time(res_time[0]) == 'Bell':
        mixer.music.play()
        print("Bell RANG")
    time.sleep(1)
