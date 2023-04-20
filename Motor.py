import RPi.GPIO as GPIO
import time
from threading import Thread

class Motor:
  def __init__(self):
      GPIO.setmode(GPIO.BCM)
      self.out1 = 2
      self.out2 = 3
      self.out3 = 4
      self.out4 = 17

      # careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
      self.step_sleep = 0.001

      self.step_count = 200

      self.stopped = False

      # setting up
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(self.out1, GPIO.OUT)
      GPIO.setup(self.out2, GPIO.OUT)
      GPIO.setup(self.out3, GPIO.OUT)
      GPIO.setup(self.out4, GPIO.OUT)

      # initializing
      GPIO.output(self.out1, GPIO.LOW)
      GPIO.output(self.out2, GPIO.LOW)
      GPIO.output(self.out3, GPIO.LOW)
      GPIO.output(self.out4, GPIO.LOW)

  def start(self):
    GPIO.setmode(GPIO.BCM)
    Thread(target=self.show, args=()).start()
    return self
  
  def rotate_once(self):
      i = 0
      for i in range(self.step_count):
          if i % 4 == 0:
              GPIO.output(self.out4, GPIO.HIGH)
              GPIO.output(self.out3, GPIO.LOW)
              GPIO.output(self.out2, GPIO.LOW)
              GPIO.output(self.out1, GPIO.LOW)
          elif i % 4 == 1:
              GPIO.output(self.out4, GPIO.LOW)
              GPIO.output(self.out3, GPIO.LOW)
              GPIO.output(self.out2, GPIO.HIGH)
              GPIO.output(self.out1, GPIO.LOW)
          elif i % 4 == 2:
              GPIO.output(self.out4, GPIO.LOW)
              GPIO.output(self.out3, GPIO.HIGH)
              GPIO.output(self.out2, GPIO.LOW)
              GPIO.output(self.out1, GPIO.LOW)
          elif i % 4 == 3:
              GPIO.output(self.out4, GPIO.LOW)
              GPIO.output(self.out3, GPIO.LOW)
              GPIO.output(self.out2, GPIO.LOW)
              GPIO.output(self.out1, GPIO.HIGH)

          time.sleep(self.step_sleep)

  def show(self): 
    time.sleep(0.1)
    while(not self.stopped):
       self.rotate_once()
      

  def stop(self):
    # indicate that the thread should be stopped
    self.stopped = True
    
