import time

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, GPIO.LOW)

time.sleep(0.25)

GPIO.output(12, GPIO.HIGH)
GPIO.cleanup()