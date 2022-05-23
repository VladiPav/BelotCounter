import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

sleeptime = .1

relayPin = 14
btnPin = 5

GPIO.setup(relayPin, GPIO.OUT)
GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(relayPin, False)
try:
    while True:
        GPIO.output(relayPin, not GPIO.input(btnPin))
        sleep(sleeptime)
finally:
    GPIO.output(relayPin, False)
    GPIO.cleanup()