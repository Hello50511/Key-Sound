# -*- coding: utf-8 -*-

import keyboard
from playsound import playsound

while True:
    if keyboard.read_key():
        playsound('key.wav', block=False)
