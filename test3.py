
import numpy as np
import cv2 
import os
from VideoStream import VideoStream

path = 'C:\\Users\\vladi\\OneDrive\\School\\OpenCV\\BelotCounter\\MyCardImages'
suitContours = []
rankContours = []
suits = []
ranks = []
for suit in os.listdir(path + "\\SuitImages"):
    img = cv2.imread(f'{path}\\SuitImages\\{suit}', 0)
    thresholded = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
    contours = cv2.findContours(thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    suitContours.append(contours[1])
    suits.append(os.path.splitext(suit)[0])
    # cv2.drawContours(img, contours, 1, (0, 255, 0), 5)
    # cv2.imshow(os.path.splitext(suit)[0], img)

for rank in os.listdir(path + "\\RankImages"):
    img = cv2.imread(f'{path}\\RankImages\\{rank}', 0)
    thresholded = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
    contours = cv2.findContours(thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
    rankContours.append(contours[1])
    ranks.append(os.path.splitext(rank)[0])


video = VideoStream(0).start()

f = set()

threshold = 0.007

while True:
    currSuit = "Unknown"
    img = video.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    i = 0
    j = 0
    _, imgbw = cv2.threshold(imgGray, 120, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(imgbw, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    for i in range(11):
        for j in range(4):
            if(cv2.matchShapes(suitContours[j], contours[i], 1, 0) < threshold):
                #cv2.drawContours(img, contours, i, (0, 255, 0), 3)
                print(suits[j])
    #cv2.imshow("img", img)
    
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
video.stop()

