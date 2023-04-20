import RPi.GPIO as GPIO
from time import sleep
import numpy as np
import cv2 
import os
from VideoStream import VideoStream

from Motor import Motor

def count(cards, gameType):
    total = 0

    for i in cards:
        if i[0] == "Jack":
            if gameType == "All trumps" or i[1] + "s" == gameType:
                total += 20
            else:
                total += 2
        elif i[0] == "Nine":
            if gameType == "All trumps" or i[1] + "s" == gameType:
                total += 14
        elif i[0] == "Ace":
            total += 11
        elif i[0] == "Ten":
            total += 10
        elif i[0] == "King":
            total += 4
        elif i[0] == "Queen":
            total += 3
    return total

def run(gameType, display):
    display.setNumber(0)
    GPIO.setmode(GPIO.BCM)
    flashPin = 25

    GPIO.setup(flashPin, GPIO.OUT)
    GPIO.output(flashPin, False)

    sleep(0.2)

    motor = Motor.start()


    path = '/home/VladiRPi/BelotCounter/MyCardImages'
    suitImages = []
    rankImages = []
    suits = []
    ranks = []
    for suit in sorted(os.listdir(path + "/SuitImages")):
        img = cv2.imread(f'{path}/SuitImages/{suit}', 0)
        thresholded = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
        contours = cv2.findContours(thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        suitImages.append(contours[1])
        suits.append(os.path.splitext(suit)[0])


    for rank in sorted(os.listdir(path + "/RankImages")):
        img = cv2.imread(f'{path}/RankImages/{rank}', 0)
        thresholded = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
        contours = cv2.findContours(thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[0]
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        rankImages.append(contours[1])
        ranks.append(os.path.splitext(rank)[0])

    video = VideoStream(0).start()

    detectedCards = set()
    current = set()

    suitThreshold = 0.07
    rankThreshold = 0.1
    counter = 0
    current_count = 0
    currCard = "Unknown of Unknowns"
    try:
        GPIO.output(flashPin, True)
        while True:
            currRank = "Unknown"
            currSuit = "Unknown"
            img = video.read()
            if img is None:
                print("No frame")
                break
            img = cv2.GaussianBlur(img, (5, 5), 0, 0)
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            imgbw = cv2.threshold(imgGray, 120, 255, cv2.THRESH_BINARY)[1]

            suitHalf = imgbw[70: 185, 40:170]
            suitContours = cv2.findContours(suitHalf, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
            suitContours = sorted(suitContours, key=cv2.contourArea, reverse=True)
            rankHalf = imgbw[45:185, 150:325]
            rankHalf = cv2.erode(rankHalf, np.ones((5,5), np.uint8))
            rankContours = cv2.findContours(rankHalf, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[0]
            rankContours = sorted(rankContours, key=cv2.contourArea, reverse=True)
            for i in range(1, min(len(suitContours),3)):
                if cv2.contourArea(suitContours[i]) > 2000:
                    min_suit_threshold = 10
                    for j in range(len(suits)):
                        current_suit_threshold = cv2.matchShapes(suitImages[j], suitContours[1], 1, 0)
                        if current_suit_threshold < suitThreshold:
                            if current_suit_threshold < rankThreshold:
                                if min_suit_threshold > current_suit_threshold:
                                    min_suit_threshold = current_suit_threshold
                                    currSuit = suits[j]
            for i in range(1, min(len(rankContours),3)):
                if cv2.contourArea(rankContours[i]) > 500:
                    x,y,w,h = cv2.boundingRect(rankContours[i])
                    min_rank_threshold = 10
                    for j in range(len(ranks)):
                        current_rank_threshold = cv2.matchShapes(rankImages[j], rankContours[1], 1, 0)
                        if ranks[j] == "Jack" or  ranks[j] == "King":
                            rankThreshold = 1
                            sleep(0.0005)
                        if current_rank_threshold < rankThreshold:
                            if min_rank_threshold > current_rank_threshold:
                                min_rank_threshold = current_rank_threshold
                                currRank = ranks[j]
                        if ranks[j] == "Jack" or  ranks[j] == "King":
                            rankThreshold = 0.1
            currCard = (currRank, currSuit)
            if "Unknown" not in currCard and currCard not in detectedCards:
                counter += 1
                current.add(currCard)
                #print(currCard)
                if counter % 3 == 0:
                    if len(current) == 1:
                        detectedCards.add(currCard)
                        current_count = count(detectedCards, gameType)
                        display.setNumber(current_count)
                        #print(str(counter) + ": " + str((currRank, currSuit)))
                    current.clear()
            if currRank == "EOL":
                break
            motor.stop()
            cv2.waitKey(10)
    except KeyboardInterrupt:
        video.stop()
        motor.stop()
        GPIO.output(flashPin, False)
    finally:
        video.stop()
        motor.stop()
        GPIO.output(flashPin, False)