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
        press = input("f to go forward, s to stop, b to go backwards, r to go right, l to go left, and e to exit the program")
        time.sleep(0.5)
        
        if press == "f":
            tank_pair.on(left_speed = 50, right_speed = 50)
            print("going forward")
        
        elif press == "s":
            tank_pair.on(left_speed = 0, right_speed = 0)
            print("stopping")

        elif press == "b":
            tank_pair.on(left_speed = -50, right_speed = -50)
            print("going backwards")

        elif press == "r":
            tank_pair.on(left_speed = 50, right_speed = 0)
            print("going right")

        elif press == "l":
            tank_pair.on(left_speed = 0, right_speed = 50)
            print("going left")

        elif press == "e":
            break
            tank_pair.on(left_speed = 0, right_speed = 0)


except(KeyboardInterrupt):
    print('interrupt')
    tank_pair.on(left_speed = 0, right_speed = 0)
    
    
    
    
