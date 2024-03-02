# This will hold functions used for the User (hand recognition)

import sys
import cv2
from cvzone.HandTrackingModule import HandDetector

def main():
    detector = HandDetector(detectionCon=0.8, maxHands=1)
    video = cv2.VideoCapture(0)
    
    video.set(3, 640)
    video.set(4, 480)

    currently_running = True

    while not currently_running:
        #add a goodbye message?
        video.release()
        cv2.destroyAllWindows()
        sys.exit()

    ret, frame = video.read()
    hands, img = detector.findHands(frame)

    imgScaled = cv2.resize(img, (0, 0), None, 0.533, 0.533)

    cv2.rectangle(img, (0, 480), (300, 425), (0, 0, 0), -2)
    cv2.rectangle(img, (640, 480), (300, 425), (0, 0, 0), -2)

    if hands:
        lmlist = hands[0]
        fingerUp = detector.fingersUp(lmlist)

        #this one will open default web browser
        if fingerUp == [0, 1, 0, 0, 0]:
            #open web browser
            return 0 #i hate looking at red squiggles
        
        #this one will open notepad
        if fingerUp == [0, 1, 1, 0, 0]:
            #open notepad
            return 0
        
        #this one will open up the command prompt
        if fingerUp == [0, 1, 1, 1, 0]:
            #open terminal
            return 0
        
        #this one will open up the computer settings
        if fingerUp == [0, 1, 1, 1, 1]:
            #open settings
            return 0
        
        #this one will center the cat and make it larger
        if fingerUp == [1, 1, 1, 1, 1]:
            #make cat larger and center it
            return 0
        
        #this will allow user to pick up the cat
        if fingerUp == [1, 1, 0, 0, 0]:
            #pick up cat
            return 0
        
        cv2.imshow("Camera", imgScaled)
        
if __name__ == '__main__': 
    main()