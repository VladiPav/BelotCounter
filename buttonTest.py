import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

sleeptime = .1

ledPin = 23
btnPin = 18

GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    GPIO.output(ledPin, GPIO.input(btnPin))
    sleep(sleeptime)