import RPi.GPIO as GPIO
from time import sleep
from threading import Thread
import cv2
class Display:

    def __init__(self, number = 0):
        GPIO.setmode(GPIO.BCM)
        self.number = number
        self.sleeptime = .006
        self.segments = (21, 20, 16, 12, 7,  26, 19)

        self.common = (5, 6, 13)


        self.digits = (
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
        for i in self.segments:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, True)

        for i in self.common:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, False)

        self.stopped = False
        
    def setNumber(self, number):
        self.number = number

    def start(self):
        GPIO.setmode(GPIO.BCM)
        Thread(target=self.show, args=()).start()
        return self

    def show(self):
        # keep looping infinitely until the thread is stopped
        while not self.stopped:
            temp = self.number
            for i in self.common:
                GPIO.output(i, True)
                GPIO.output(self.segments, self.digits[temp % 10])
                temp //= 10
                sleep(self.sleeptime)
                GPIO.output(i, False)
    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True
