import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)


sleeptime = .006
segments = (21, 20, 26, 19, 16, 13, 6)

common = (2, 3, 17)
btnPin = 5


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

GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

curr = 0
prevInput = 0
try:
    while True:
        input = GPIO.input(btnPin)
        temp = curr
        for i in common:
            GPIO.output(i, True)
            GPIO.output(segments, digits[temp % 10])
            temp //= 10
            sleep(sleeptime)
            GPIO.output(i, False)
        if (not prevInput) and input == GPIO.HIGH:
            curr += 1
        prevInput = input
        
        
finally:
    for i in segments:
        GPIO.output(i, True)
    for i in common:
        GPIO.output(i, False)
    GPIO.cleanup()