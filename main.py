import RPi.GPIO as GPIO
from time import sleep
from Display import Display

from run import run
GPIO.setmode(GPIO.BCM)
while True:
    GPIO.setmode(GPIO.BCM)

    sleeptime = .1

    ledPins = (17, 27, 22, 14, 15, 18)
    gameType = ("Clubs", "Diamonds", "Hearts", "Spades", "No trumps", "All trumps")
    buttonPin = 9
    
    startButtonPin = 8


    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(startButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    

    for i in ledPins:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, False)
    lastState = GPIO.input(buttonPin)
    counter = 0

    display = Display().start()

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
        
        run(gameType[counter], display)
    GPIO.cleanup()
    display.stop()
