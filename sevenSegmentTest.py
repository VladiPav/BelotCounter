import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)


sleeptime = .001
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
temp = curr

try:
    while True:
        for i in common:
            GPIO.output(i, True)
            counter = 0
            for j in segments:
                GPIO.output(j, digits[temp%10][counter])
                counter += 1
            temp /= 10
        sleep(sleeptime)
        
finally:
    for i in segments:
        GPIO.output(i, True)
    for i in common:
        GPIO.output(i, False)
    GPIO.cleanup()