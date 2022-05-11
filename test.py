from pydoc import classname
import numpy as np
import cv2 
import os

path = 'C:\\Users\\vladi\\OneDrive\\School\\OpenCV\\Project\\MyCardImages'
images = []
classNames = []
myList = os.listdir(path)
for cl in myList:
    imgCur = cv2.imread(f'{path}/{cl}', 0)
    images.append(imgCur)
    classNames.append(os.path.splitext(cl)[0])


video = cv2.VideoCapture(0)

while True:

    _, im = video.read()
    threshold = 0.87
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    i = 0
    while i < len(images):
        template = images[i]
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(imgray,template,cv2.TM_CCOEFF_NORMED)
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(im, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
            cv2.putText(im, classNames[i], (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("contours", im)
        i += 1
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

