import time

import RPi.GPIO as GPIO

relayPin = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin, GPIO.OUT)
GPIO.output(relayPin, GPIO.HIGH)

time.sleep(1)
GPIO.output(relayPin, GPIO.LOW)

time.sleep(1)
GPIO.output(relayPin, GPIO.HIGH)

time.sleep(1)
GPIO.output(relayPin, GPIO.LOW)

time.sleep(1)
GPIO.output(relayPin, GPIO.HIGH)

time.sleep(1)
GPIO.cleanup()