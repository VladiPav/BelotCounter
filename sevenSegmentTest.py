import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

sleeptime = .1
segments = (21, 20, 26, 19, 16, 13, 6)

for i in segments:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, False)

try:
    while True:
        for i in segments:
            GPIO.output(i, True)
        sleep(sleeptime)
        
finally:
    for i in segments:
        GPIO.output(i, False)
    GPIO.cleanup()