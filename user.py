# This will hold functions used for the User (hand recognition)

import sys
import cv2
from cvzone.HandTrackingModule import HandDetector
import os
import webbrowser


#tasks
def open_google():
    url = 'http://google.com'
    webbrowser.open_new_tab(url)

def open_notepad():
    os.system("notepad.exe")

def open_terminal(): 
    os.system("start cmd.exe")

def open_settings(): 
    os.popen("start ms-settings:")


video = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

def main():
    #video = cv2.VideoCapture(0)
    while True:
        #detector = HandDetector(detectionCon=0.8, maxHands=1)
        #video = cv2.VideoCapture(0)
    
        video.set(3, 640)
        video.set(4, 480)

        currently_running = True

        #while not currently_running:
            #add a goodbye message?
            #video.release()
            #cv2.destroyAllWindows()
            #sys.exit()

        ret, frame = video.read()
        hands, img = detector.findHands(frame)

        imgScaled = cv2.resize(img, (0, 0), None, 0.533, 0.533)

        cv2.rectangle(img, (0, 480), (300, 425), (0, 0, 0), -2)
        cv2.rectangle(img, (640, 480), (300, 425), (0, 0, 0), -2)

        cv2.imshow("Camera", imgScaled)

        if hands:
            lmlist = hands[0]
            fingerUp = detector.fingersUp(lmlist)

            #this one will open default web browser
            if fingerUp == [0, 1, 0, 0, 0]:
                #open web browser
                open_google()
        
            #this one will open notepad
            if fingerUp == [0, 1, 1, 0, 0]:
                #open notepad
                open_notepad()
        
            #this one will open up the command prompt
            if fingerUp == [0, 1, 1, 1, 0]:
                #open terminal
                open_terminal()
        
            #this one will open up the computer settings
            if fingerUp == [0, 1, 1, 1, 1]:
                #open settings
                open_settings()
        
            #this one will center the cat and make it larger
            #if fingerUp == [1, 1, 1, 1, 1]:
                #make cat larger and center it
            #     return 0
        
            #this will allow user to pick up the cat
            # if fingerUp == [1, 1, 0, 0, 0]:
            #     #pick up cat
            #     return 0
        
            #this will allow the user to close the program
            if fingerUp == [1, 0, 0, 0, 0]:
                break

    video.release()
        
if __name__ == '__main__': 
    main()