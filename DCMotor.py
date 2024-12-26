import RPi.GPIO as GPIO
from time import sleep

# Pins for Motor Driver Inputs 
Motor1A = 17
Motor2A = 18
Motor1E = 21
 
def setup():
	GPIO.setmode(GPIO.BCM)				# GPIO Numbering
	GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
	GPIO.setup(Motor2A,GPIO.OUT)
	GPIO.setup(Motor1E,GPIO.OUT)
 
def loop():
	print("Going Clockwise")
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)
	sleep(5)

        print("Stop")
        GPIO.output(Motor1E,GPIO.LOW)
	sleep(5)

	print("Going Counter Clockwise")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.HIGH)
 	sleep(5)

	print("Stop")
	GPIO.output(Motor1E,GPIO.LOW)
	sleep(5)

def destroy():	
	GPIO.cleanup()

if __name__ == '__main__':     # Program start from here
	setup()
	try:
    		loop()
  	except KeyboardInterrupt:
		destroy()
