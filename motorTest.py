import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

sleeptime = .1

motorPin = 18
btnPin = 5

GPIO.setup(motorPin, GPIO.OUT)
GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(motorPin, False)
try:
    while True:
        GPIO.output(motorPin, GPIO.input(btnPin))
        print (GPIO.input(btnPin))
        sleep(sleeptime)
finally:
    GPIO.output(motorPin, False)
    GPIO.cleanup()