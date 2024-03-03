import cv2
import mouse
from cvzone.HandTrackingModule import HandDetector
import numpy as np

detector = HandDetector(detectionCon = 0.9, maxHands = 1)

video = cv2.VideoCapture(0)
camw, camh = 640, 480
video.set(3, camw)
video.set(4, camh)

while True:
    success, img = video.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)
    if hands:
        lmlist = hands[0]["lmList"]
        x, y = lmlist[8][0], lmlist[8][1]
        cv2.circle(img, (x, y), 5, (0, 255, 255), 2)
        conv_x = int(np.interp(x, (0, camw), (0, 1536)))
        conv_y = int(np.interp(y, (0, camh), (0, 864)))
        mouse.move(x, y)

    cv2.imshow("Hi, user!", img)
    cv2.waitKey(1)