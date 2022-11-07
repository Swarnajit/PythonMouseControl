import cv2
import mediapipe as mp
import numpy as np
import HandTrackingModule as htm
import time

###############################
wCam, hCam = 648, 488
pTime = 0
detector = htm.handDetector(maxHands=1)
###############################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

while True:
    # 1. Find hand landmarks
    success, img = cap.read()
    img = detector.findHands(img)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20 , 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    cv2.imshow('Image', img)
    cv2.waitKey(1)