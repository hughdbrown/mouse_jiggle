#!/usr/bin/env python3

from datetime import datetime
from random import randrange
from time import sleep
 
import pyautogui

JIGGLE_INTERVAL = 300

def main():
    while True:
        x = randrange(-3, 4)
        y = randrange(-3, 4)
        print(f"{datetime.now()}")
        pyautogui.move(x, y)
        pyautogui.move(-x, -y)
        sleep(JIGGLE_INTERVAL)

if __name__ == '__main__':
    main()
