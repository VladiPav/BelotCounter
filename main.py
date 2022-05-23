import numpy as np
import cv2 
import os
from VideoStream import VideoStream

path = 'C:\\Users\\vladi\\OneDrive\\School\\OpenCV\\BelotCounter\\MyCardImages\\SuitImages'
SuitImages = []
RankImages = []
suits = []
ranks = []
for suit in os.listdir(path + "/SuitImages"):
    imgCur = cv2.imread(f'{path}/SuitImages/{suit}', 0)
    SuitImages.append(imgCur)
    suits.append(os.path.splitext(suit)[0])

for rank in os.listdir(path + "/RankImages"):
    imgCur = cv2.imread(f'{path}/RankImages/{suit}', 0)
    RankImages.append(imgCur)
    ranks.append(os.path.splitext(rank)[0])


video = VideoStream(0).start()

f = set()

while True:
    print(f)
    im = video.read()
    threshold = 0.87
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    i = 0
    counter = 0
    while i < len(RankImages):
        template = RankImages[i]
        
    """while i < len(images):
        template = images[i]
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(imgray,template,cv2.TM_CCOEFF_NORMED)
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(im, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
            cv2.putText(im, Suit[i], (50,(counter+1)*20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            sensitivity = 100
            f.add(Suit[i])
        counter += 1
        cv2.imshow("contours", im)
        i += 1"""
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.stop()

