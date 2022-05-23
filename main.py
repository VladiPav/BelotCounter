
import numpy as np
import cv2 
import os
from VideoStream import VideoStream

def is_template_in_image(img, template):

    result = cv2.matchTemplate(img, template, cv2.TM_SQDIFF)

    min_val = cv2.minMaxLoc(result)[0]

    thr = 10e-6

    return min_val <= thr


path = 'C:\\Users\\vladi\\OneDrive\\School\\OpenCV\\BelotCounter\\MyCardImages'
suitImages = []
rankImages = []
suits = []
ranks = []
for suit in os.listdir(path + "/SuitImages"):
    imgCur = cv2.imread(f'{path}/SuitImages/{suit}', 0)
    suitImages.append(imgCur)
    suits.append(os.path.splitext(suit)[0])

for rank in os.listdir(path + "/RankImages"):
    imgCur = cv2.imread(f'{path}/RankImages/{suit}', 0)
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
    while j < len(suitImages):
        template = suitImages[j]
        if(is_template_in_image(img, template)):
            currSuit = suits[j]
    print(currSuit)
    cv2.imshow("img", img)
            
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

