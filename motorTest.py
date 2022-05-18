import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

sleeptime = .1

motorPin = 14

GPIO.setup(motorPin, GPIO.OUT)
GPIO.output(motorPin, False)

try:
    while True:
        GPIO.output(motorPin, True)
        sleep(sleeptime)
finally:
    GPIO.output(motorPin, False)
    GPIO.cleanup()