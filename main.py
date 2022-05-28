
import numpy as np
import cv2 
import os
from VideoStream import VideoStream

path = 'C:\\Users\\vladi\\OneDrive\\School\\OpenCV\\BelotCounter\\MyCardImages'
suitImages = []
rankImages = []
suits = []
ranks = []
for suit in os.listdir(path + "\\SuitImages"):
    imgCur = cv2.imread(f'{path}\\SuitImages\\{suit}', 0)
    suitImages.append(imgCur)
    suits.append(os.path.splitext(suit)[0])

for rank in os.listdir(path + "\\RankImages"):
    imgCur = cv2.imread(f'{path}\\RankImages\\{rank}', 0)
    rankImages.append(imgCur)
    ranks.append(os.path.splitext(rank)[0])


video = VideoStream(0).start()

f = set()
while True:
    currSuit = "Unknown"
    img = video.read()
    threshold = 0.87
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    i = 0
    j = 0
    _, imgbw = cv2.threshold(imgGray, 120, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(imgbw, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    
    cv2.drawContours(img, contours, 5, (0,255,0), 3)
    cv2.imshow("img", img)
    
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
video.stop()

