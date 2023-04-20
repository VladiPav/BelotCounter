import RPi.GPIO as GPIO
from time import sleep
from Display import Display

from run import run
GPIO.setmode(GPIO.BCM)
last_count = 0
while True:
    GPIO.setmode(GPIO.BCM)

    sleeptime = .1

    ledPins = (8, 11, 9, 10, 22, 27)
    gameType = ("Clubs", "Diamonds", "Hearts", "Spades", "No trumps", "All trumps")
    buttonPin = 23
    
    startButtonPin = 24


    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(startButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    

    for i in ledPins:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, False)
    lastState = GPIO.input(buttonPin)
    counter = 0
    print("\nCREATING DISPLAY\n\n")
    display = Display(last_count).start()

    try:
        while GPIO.input(startButtonPin):
            input = GPIO.input(buttonPin)
            GPIO.output(ledPins[counter], True)
            if input and not lastState:
                GPIO.output(ledPins[counter], False)
                if counter + 1 < len(ledPins):
                    counter += 1
                else:
                    counter = 0
            lastState = input
            sleep(sleeptime)
    finally:
        for i in ledPins:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, False)
        print("STARTING")
        last_count = run(gameType[counter], display)
    GPIO.cleanup()
    display.stop()
