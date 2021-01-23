import cv2
import numpy as np
import utili

webcam = False
path = 'img1.jpg'
cap = cv2.VideoCapture(0)
cap.set(10,160)
cap.set(3,1920)
cap.set(4,1080)
scale = 3
wP = 210 * scale
hP = 297 * scale

while True:
    if webcam : success,img = cap.read()
    else : img = cv2.imread(path)

    imgContours, finalContours = utili.getContours(img,minArea=50000,filter=4)

    if len(finalContours) != 0:
        biggest = finalContours[0][2]
        imgWrap = utili.warpImg(img, biggest, wP, hP)
        cv2.imshow('A4', imgWrap)
        imgContours2, finalContours2 = utili.getContours(imgWrap, minArea=2000, filter=4, cThr = [50,50],draw=False)

        if len(imgContours2) != 0:
            for obj in imgContours2:
                cv2.polylines(imgContours2,[obj[2]],True,(0,255,0),2)
                nPoints = utili.reorder(obj[2])
                nW = round((utili.findMeasurement(nPoints[0][0]//scale,nPoints[1][0]//scale)/10),1)
                nH = round((utili.findMeasurement(nPoints[0][0] // scale, nPoints[2][0] // scale) / 10),1)

        cv2.imshow('A4', imgContours2)

    img = cv2.resize(img,(0,0),None,0.5,0.5)
    cv2.imshow('Original', img)
    cv2.waitKey(1)