import time

import RPi.GPIO as GPIO

relayPin = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin, GPIO.OUT)

try:
    while True:
        GPIO.output(relayPin, False)
        time.sleep(2)   
        GPIO.output(relayPin, True)
finally:
    GPIO.output(relayPin, True)
    GPIO.cleanup()