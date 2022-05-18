import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)


sleeptime = .0001
segments = (21, 20, 26, 19, 16, 13, 6)

common = (2, 3, 17)

digits = (
    (0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 1, 1, 1, 1),
    (0, 0, 1, 0, 0, 1, 0),
    (0, 0, 0, 0, 1, 1, 0),
    (1, 0, 0, 1, 1, 0, 0),
    (0, 1, 0, 0, 1, 0, 0),
    (0, 1, 0, 0, 0, 0, 0),
    (0, 0, 0, 1, 1, 1, 1),
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 1, 0, 0)
)

for i in segments:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, True)

for i in common:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, False)

curr = 123

try:
    while True:
        temp = curr
        for i in common:
            GPIO.output(i, True)
            GPIO.output(segments, digits[temp % 10])
            temp //= 10
            sleep(sleeptime)
            GPIO.output(i, False)
        
finally:
    for i in segments:
        GPIO.output(i, True)
    for i in common:
        GPIO.output(i, False)
    GPIO.cleanup()