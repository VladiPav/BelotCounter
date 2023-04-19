import RPi.GPIO as GPIO
from time import sleep

stepPin = 2

GPIO.setmode(GPIO.BCM)

GPIO.setup(stepPin, GPIO.OUT)
GPIO.output(stepPin, False)

try:
    for i in range(50):
        GPIO.output(stepPin, True)
        sleep(0.01)
        GPIO.output(stepPin, False)
        sleep(0.01)
finally:
    GPIO.output(stepPin, False)
    GPIO.cleanup()
