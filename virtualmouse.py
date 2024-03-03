import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Controller
import pyautogui

import tasks
import virtualkeyboard

def main():
    cap = cv2.VideoCapture(0)
    screen_width, screen_height = pyautogui.size()

    detector = HandDetector(detectionCon=1)

    while True: 
        success, img = cap.read()
        frame_height, frame_width, _ = img.shape
        img = cv2.flip(img, 1)
        img = detector.findHands(img)
        lmList, bboxInfo = detector.findPosition(img)

        if lmList:
            l, _, _ = detector.findDistance(4, 8, img, draw=False)
            fingerup = detector.fingersUp()
            x_finger = lmList[8][0]
            y_finger = lmList[8][1]
            
            if fingerup == [0, 1, 1, 1, 1]:
                break
            if fingerup == [0, 0, 0, 0, 1]:
                virtualkeyboard.main(cap)

            # thumb and pointer close to each other
            if l < 20:
                pyautogui.mouseDown()
            elif l < 100:
                index_x = screen_width/frame_width*x_finger
                index_y = screen_height/frame_height*y_finger
                pyautogui.moveTo(index_x, index_y)
            else: 
                pyautogui.mouseUp()  
                

        cv2.imshow("Image", img)
        cv2.setWindowProperty("Image", cv2.WND_PROP_TOPMOST, 1)
        cv2.waitKey(1)

main()