import numpy as np
import cv2 
import os
from VideoStream import VideoStream

path = 'C:\\Users\\vladi\\OneDrive\\School\\OpenCV\\BelotCounter\\MyCardImages'
images = []
classNames = []
myList = os.listdir(path)
for cl in myList:
    imgCur = cv2.imread(f'{path}/{cl}', 0)
    #imgCur = cv2.threshold(imgCur, 140, 255, cv2.THRESH_BINARY)
    images.append(imgCur)
    classNames.append(os.path.splitext(cl)[0])


video = VideoStream(0).start()

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

f = set()

while True:
    print(f)
    im = video.read()
    threshold = 0.87
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    #imBlackNWhite = cv2.threshold(imgray, 140, 255, cv2.THRESH_BINARY)
    i = 0
    counter = 0
    while i < len(images):
        template = images[i]
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(imgray,template,cv2.TM_CCOEFF_NORMED)
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(im, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
            cv2.putText(im, classNames[i], (50,(counter+1)*20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            sensitivity = 100
            f.add(classNames[i])
        counter += 1
        cv2.imshow("contours", im)
        i += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.stop()

