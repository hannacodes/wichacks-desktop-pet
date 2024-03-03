import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import numpy as np
import cvzone
from pynput.keyboard import Controller
# pip install cvzone==1.4.1
# pip install pynput
# pip install mediapipe

import tasks

def drawAll(img, buttonList):
        for button in buttonList:
            x, y = button.pos
            w, h = button.size
            cv2.rectangle(img, button.pos, (x + w, y + h), (169, 169, 169), cv2.FILLED)
            cv2.putText(img, button.text, (x + 20, y + 65),
                        cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
        return img

class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text

def setup(): 
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    detector = HandDetector(detectionCon=1)
    keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
            ["Z", "X", "C", "V", "B", "N", "M", " ", "<", ">"]]

    keyboard = Controller()

    buttonList = []
    for i in range(len(keys)):
        for j, key in enumerate(keys[i]):
            buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

    return cap, detector, buttonList, keyboard

def show_keyboard(cap, detector, buttonList, keyboard, finalText):
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)
    img = drawAll(img, buttonList)

    if lmList:
        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                # hover 
                cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (117, 117, 117), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65),
                            cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                l, _, _ = detector.findDistance(8, 12, img, draw=False)

                ## when clicked
                if l < 30:
                    if button.text == ">":
                        return finalText, True
                    if button.text == "<":
                        length = len(finalText)
                        removeText = finalText[0:length-1]
                        finalText = removeText
                    else:
                        keyboard.press(button.text)
                        print(button.text)
                        
                        finalText += button.text
                    sleep(0.15)
    cv2.rectangle(img, (50, 350), (700, 450), (169, 169, 169), cv2.FILLED)
    cv2.putText(img, finalText, (60, 430),
            cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

    return finalText, False

#driver = tasks.open_google()
cap, detector, buttonList, keyboard = setup()
finalText = ""
while True: 
    finalText, done = show_keyboard(cap, detector, buttonList, keyboard, finalText)
    if done:
        print(finalText)
        break
#tasks.search_google(driver, text)