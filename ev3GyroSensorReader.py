#!/usr/bin/env python3

from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.button import Button
from time import sleep
import logging

logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s %(levelname)5s: %(message)s')
log = logging.getLogger(__name__)
log.info('Starting GyroSensor Reader Program')


any_button = Button()
gyro_sensor = GyroSensor()
cs = ColorSensor()

try:
    while not any_button.any():
        angle = gyro_sensor.angle
        intensity = cs.reflected_light_intensity        
        
        log.info('Angle in Degree ' + str(angle) + ' Reflected light intensity ' + str(intensity))

        #gyro_sensor.reset()
        gyro_sensor.wait_until_angle_changed_by(90)

        change_in_angle = abs(gyro_sensor.angle - angle)

        log.info('Angle Changed by ' + str(change_in_angle))

        sleep(0.5)

except(GracefulShutdown, Exception) as e:
    log.exception(e)

log.info('Existing Gyro Sensor Reader Program')
