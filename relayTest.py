
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

sleeptime = .1

relayPin = 14
btnPin = 5

GPIO.setup(relayPin, GPIO.OUT)
GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(relayPin, GPIO.LOW)
try:
    while True:
        GPIO.output(relayPin, GPIO.LOW)
        sleep(2)
        GPIO.output(relayPin, GPIO.HIGH)
finally:
    GPIO.output(relayPin, GPIO.LOW)
    GPIO.cleanup()