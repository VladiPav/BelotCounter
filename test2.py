import cv2
import os
import numpy as np




path = 'C:\\Users\\vladi\\OneDrive\\School\\OpenCV\\BelotCounter\\MyCardImages\\RankImages'
images = []
classNames = []
myList = os.listdir(path)
for cl in myList:
    imgCur = cv2.imread(f'{path}/{cl}', 0)
    images.append(imgCur)
    classNames.append(os.path.splitext(cl)[0])
    cv2.waitKey(1)

counter = 0
for i in images:
    contours = cv2.findContours(i, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = cv2.boundingRect(i)
    rankImg = i[y:y+h, x:x+w]
    rankImg = cv2.erode(rankImg, np.ones((5,5), np.uint8))
    cv2.imwrite(os.path.join(path, classNames[counter] + ".png"), rankImg)
    counter += 1
    cv2.waitKey(1)