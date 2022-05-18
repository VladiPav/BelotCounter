import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)


sleeptime = .001
segments = (21, 20, 26, 19, 16, 13, 6)

common = (2, 3, 3)

for i in segments:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, True)

for i in common:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, False)

try:
    while True:
        for i in common:
            GPIO.output(i, True)
            for j in segments:
                GPIO.output(j, False)
            GPIO.output(i, False)
        sleep(sleeptime)
        
finally:
    for i in segments:
        GPIO.output(i, True)
    GPIO.cleanup()