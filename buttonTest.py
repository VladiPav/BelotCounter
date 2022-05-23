import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

sleeptime = .1

ledPin = 12
btnPin = 5

GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(ledPin, False)
try:
    while True:
        GPIO.output(ledPin, GPIO.input(btnPin))
        sleep(sleeptime)
finally:
    GPIO.output(ledPin, False)
    GPIO.cleanup()