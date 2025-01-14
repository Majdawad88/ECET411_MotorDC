#git clone https://github.com/Majdawad88/ECET411_MotorDC.git

import RPi.GPIO as GPIO
from time import sleep

# Pins for Motor Driver Inputs

Motor1E = 13
Motor1A = 19
Motor2A = 26


def setup():
        GPIO.setmode(GPIO.BCM)                          # GPIO Numbering
        GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
        GPIO.setup(Motor2A,GPIO.OUT)
        GPIO.setup(Motor1E,GPIO.OUT)

def loop():
        print("Going Clockwise")
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor1E,GPIO.HIGH)
        sleep(5)

        print("Stop")
        GPIO.output(Motor1E,GPIO.LOW)
        sleep(5)

        print("Going Counter Clockwise")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor1E,GPIO.HIGH)
        sleep(5)

        print("Stop")
        GPIO.output(Motor1E,GPIO.LOW)
        sleep(5)

setup()
while True:
        loop()
