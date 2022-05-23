import time

import RPi.GPIO as GPIO

relayPin = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin, GPIO.OUT)

try:
    GPIO.output(relayPin, False)
    print("False")
    time.sleep(2)   
    GPIO.output(relayPin, True)
    print("True")
    time.sleep(2)
    GPIO.output(relayPin, False)
    print("False")
    time.sleep(2)
    GPIO.output(relayPin, True)
    print("True")
    time.sleep(2)
finally:
    GPIO.output(relayPin, False)
    GPIO.cleanup()