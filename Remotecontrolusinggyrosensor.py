#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_D
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.button import Button
import time
import logging

logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s %(levelname)5s: %(message)s')
log = logging.getLogger(__name__)

gyro_sensor = GyroSensor()
tank_pair = MoveTank(OUTPUT_A, OUTPUT_D)
button = Button()


try:
    while not button.any():
        press = input("f to go forward, s to stop, b to go backwards, r to go right for 90 degrees, R to go right for 180 degrees, l to go left for 90 degrees, L to go left for 180 degrees, and e to exit the program")
        time.sleep(0.5)
        intensity = cs.reflected_light_intensity
        
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
            log.info('Angle in Degree ' + str(angle) + ' Reflected light intensity ' + str(intensity))
            print(angle)
            tank_pair.on(left_speed = 25, right_speed = 0)
            gyro_sensor.wait_until_angle_changed_by(90)
            change_in_angle = abs(gyro_sensor.angle - angle)
            log.info('Angle Changed by ' + str(change_in_angle))
            print(change in angle)
            tank_pair.on(left_speed = 0, right_speed = 0)
            print("going right for 90 degrees")

        elif press == "R":
            log.info('Angle in Degree ' + str(angle) + ' Reflected light intensity ' + str(intensity))
            print(angle)
            tank_pair.on(left_speed = 25, right_speed = 0)
            gyro_sensor.wait_until_angle_changed_by(180)
            change_in_angle = abs(gyro_sensor.angle - angle)
            log.info('Angle Changed by ' + str(change_in_angle))
            print(change in angle)
            tank_pair.on(left_speed = 0, right_speed = 0)
            print("going right for 180 degrees")

        elif press == "l":
            log.info('Angle in Degree ' + str(angle) + ' Reflected light intensity ' + str(intensity))
            print(angle)
            tank_pair.on(left_speed = 0, right_speed = 25)
            gyro_sensor.wait_until_angle_changed_by(90)
            change_in_angle = abs(gyro_sensor.angle - angle)
            log.info('Angle Changed by ' + str(change_in_angle))
            print(change in angle)
            tank_pair.on(left_speed = 0, right_speed = 0)
            print("going left for 90 degrees")

        elif press == "L":
            log.info('Angle in Degree ' + str(angle) + ' Reflected light intensity ' + str(intensity))
            print(angle)
            tank_pair.on(left_speed = 0, right_speed = 25)
            gyro_sensor.wait_until_angle_changed_by(180)
            change_in_angle = abs(gyro_sensor.angle - angle)
            log.info('Angle Changed by ' + str(change_in_angle))
            print(change in angle)
            tank_pair.on(left_speed = 0, right_speed = 0)
            print("going left for 180 degrees")

        elif press == "e":
            break
            tank_pair.on(left_speed = 0, right_speed = 0)


except(KeyboardInterrupt):
    print('interrupt')
    tank_pair.on(left_speed = 0, right_speed = 0)
