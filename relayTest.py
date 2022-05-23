import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

sleeptime = .1

relayPin = 12
btnPin = 5

GPIO.setup(relayPin, GPIO.OUT)
GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(relayPin, True)
try:
    while True:
        GPIO.output(relayPin, False)
        sleep(2)
        GPIO.output(relayPin, True)
finally:
    GPIO.output(relayPin, True)
    GPIO.cleanup()