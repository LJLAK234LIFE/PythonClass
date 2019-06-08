#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_D
from ev3dev2.button import Button
import time
import logging

logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s %(levelname)5s: %(message)s')
log = logging.getLogger(__name__)

tank_pair = MoveTank(OUTPUT_A, OUTPUT_D)
button = Button()

try:
    while not button.any():
        press = input("w to go forward, x to stop, s to go backwards, a to go right, d to go left, and t to exit the program")
        time.sleep(0.5)
        if press == "w":
            tank_pair.on(left_speed = 50, right_speed = 50)
            print("going forward")
        
        elif press == "x":
            tank_pair.on(left_speed = 0, right_speed = 0)
            print("stopping")

        elif press == "s":
            tank_pair.on(left_speed = -50, right_speed = -50)
            print("going backwards")

        elif press == "a":
            tank_pair.on(left_speed = 50, right_speed = 0)
            print("going right")

        elif press == "d":
            tank_pair.on(left_speed = 0, right_speed = 50)
            print("going left")

        elif press == "t":
            break


except(KeyboardInterrupt):
    print('interrupt')
    tank_pair.on(left_speed = 0, right_speed = 0)
