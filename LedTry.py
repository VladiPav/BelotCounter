import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

sleeptime = .1

ledPin = 12

GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, False)

try:
    while True:
        GPIO.output(ledPin, True)
        sleep(sleeptime)
finally:
    GPIO.output(ledPin, False)
    GPIO.cleanup()