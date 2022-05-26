
import math
import numpy as np
import cv2 
import os
from VideoStream import VideoStream
import Cards

path = 'C:\\Users\\vladi\\OneDrive\\School\\OpenCV\\BelotCounter\\MyCardImages'
suitImages = []
rankImages = []
suits = []
ranks = []
for suit in sorted(os.listdir(path + "\\SuitImages")):
    img = cv2.imread(f'{path}\\SuitImages\\{suit}', 0)
    thresholded = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
    contours = cv2.findContours(thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    suitImages.append(contours[1])
    # suitImages.append(thresholded)
    suits.append(os.path.splitext(suit)[0])
    # cv2.drawContours(img, contours, 1, (0, 255, 0), 5)
    # cv2.imshow(os.path.splitext(suit)[0], img)

for rank in sorted(os.listdir(path + "\\RankImages")):
    img = cv2.imread(f'{path}\\RankImages\\{rank}', 0)
    thresholded = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
    contours = cv2.findContours(thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[0]
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    rankImages.append(contours[1])
    # if rank == "Seven.png":
    #     white = cv2.imread("C:\\Users\\vladi\\OneDrive\\School\\OpenCV\\BelotCounter\\MyCardImages\\white.png",0)
    #     cv2.drawContours(white, contours, 1 , (0, 0, 255), 3)
    #     cv2.imshow("hi", white)
    # rankImages.append(img)
    ranks.append(os.path.splitext(rank)[0])
    # cv2.drawContours(img, contours, 1, (0, 255, 0), 0)
    # cv2.imshow(os.path.splitext(rank)[0], img)

avgRankBoundingArea = 25440


video = VideoStream(0).start()

f = set()

suitThreshold = 0.07
rankThreshold = 0.4
counter = 0
rankImg = 0
while True:
    currRank = "Unknown"
    currSuit = "Unknown"
    img = video.read()
    #img = img[110:220, 60:340]
    #cv2.imshow("vis", vis)
    img = cv2.GaussianBlur(img, (5, 5), 0, 0)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgbw = cv2.threshold(imgGray, 120, 255, cv2.THRESH_BINARY)[1]

    suitHalf = imgbw[70:220, 60:200]
    suitContours = cv2.findContours(suitHalf, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
    suitContours = sorted(suitContours, key=cv2.contourArea, reverse=True)
    rankHalf = imgbw[70:220, 175:340]
    rankHalf = cv2.erode(rankHalf, np.ones((5,5), np.uint8))
    rankContours = cv2.findContours(rankHalf, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[0]
    rankContours = sorted(rankContours, key=cv2.contourArea, reverse=True)
    # Checks 6 largest contours in image for a contour with a similar bounding box area to the average of a card's rank 
            
    #                 print(cv2.matchShapes(rankContours[j], contours[i], 2, 0))
    #         cv2.drawContours(img, contours, 3, (255, 0, 0), 3)
    #         print(cv2.matchShapes(rankContours[2], contours[3], 1, 0))
    #         print(ranks[2])
    #         print(ranks[5])
    # for i in range(4):
    #     cv2.drawContours(img, contours, i, (0, 0, 255), 3)


    for i in range(1, min(len(suitContours),3)):
        if cv2.contourArea(suitContours[i]) > 1000:
            min_suit_threshold = 10
        #cv2.drawContours(img, suitContours, i, (0, 0, 255), 3)
            for j in range(len(suits)):
                current_suit_threshold = cv2.matchShapes(suitImages[j], suitContours[1], 1, 0)
                if current_suit_threshold < suitThreshold:
                    if current_suit_threshold < rankThreshold:
                        if min_suit_threshold > current_suit_threshold:
                            min_suit_threshold = current_suit_threshold
                            currSuit = suits[j]
                    
                    # print(currSuit)
    
    for i in range(1, min(len(rankContours),3)):
        if cv2.contourArea(rankContours[i]) > 1000:
            x,y,w,h = cv2.boundingRect(rankContours[i])
        #cv2.drawContours(img, contours, i, (0, 0, 255), 3)
            # rankImg = rankHalf[y:y+h, x:x+w]
            # rankImg = cv2.erode(rankImg, np.ones((5,5), np.uint8))
            #cv2.rectangle(rankHalf,(x,y),(x+w,y+h),(0,255,0),2)
            min_rank_threshold = 10
            for j in range(len(ranks)):
                current_rank_threshold = cv2.matchShapes(rankImages[j], rankContours[1], 1, 0)
                #print(str(ranks[j]) + ": " + str(cv2.matchShapes(rankImages[j], rankContours[1], 1, 0)))
                if ranks[j] == "Jack":
                    white = cv2.imread("C:\\Users\\vladi\\OneDrive\\School\\OpenCV\\BelotCounter\\MyCardImages\\white.png",0)
                    cv2.drawContours(white, rankContours, 1 , (0, 0, 255), 3)
                    cv2.drawContours(white, rankImages, j , (0, 0, 255), 3)
                    cv2.imshow("hi", white)
                    # print(current_rank_threshold)
                if current_rank_threshold < rankThreshold:
                    if min_rank_threshold > current_rank_threshold:
                        min_rank_threshold = current_rank_threshold
                        currRank = ranks[j]
                # x,y,w,h = cv2.boundingRect(rankContours[i])
                # cv2.rectangle(rankHalf,(x,y),(x+w,y+h),(0,255,0),2)
                # cv2.drawContours(img, rankContours, i, (255, 0, 0), 3)
                # print(currRank)
            # if counter % 150 == 0:
            #     print(ranks[2])
            #     print(cv2.matchShapes(rankImages[2], rankContours[i], 1, 0))
    print(currRank + " of " + currSuit + "s")
    cv2.imshow("whole", img)
    cv2.imshow("suitHalf", suitHalf)
    cv2.imshow("rankHalf", rankHalf)
    # if rankImg is not None:
    #     cv2.imshow("rankimg", rankImg)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    counter += 1
    if counter == 10000:
        counter = 0
video.stop()

