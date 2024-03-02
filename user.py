# This will hold functions used for the User (hand recognition)

import sys
import cv2
from cvzone.HandTrackingModule import HandDetector
import os
import webbrowser


# tasks
def open_google():
    url = 'http://google.com'
    webbrowser.open_new_tab(url)

def open_notepad():
    os.system("notepad.exe")

def open_terminal(): 
    os.system("start cmd.exe")

def open_settings(): 
    os.popen("start ms-settings:")


def main():
    # currently_running = True
    video = cv2.VideoCapture(0)
    current = ""
    while(True):
        detector = HandDetector(detectionCon=0.8, maxHands=1)
        ret, frame = video.read() 

        cv2.imshow('Hi, user!', frame) 

        hands, img = detector.findHands(frame)
        

        # video.release()

        # cv2.rectangle(img, (0, 480), (300, 425), (0, 0, 0), -2)
        # cv2.rectangle(img, (640, 480), (300, 425), (0, 0, 0), -2)

        if hands:
            lmlist = hands[0]
            fingerUp = detector.fingersUp(lmlist)

            # this one will open default web browser
            if fingerUp == [0, 1, 0, 0, 0]:
                # open web browser
                if not current == "google":
                    open_google()
                    print(current)
                    current = "google"

            # this one will open notepad
            if fingerUp == [0, 1, 1, 0, 0]:
                # open notepad
                if not current == "notepad":
                    open_notepad()
                    print(current)
                    current = "notepad"

            # this one will open up the command prompt
            if fingerUp == [0, 1, 1, 1, 0]:
                # open terminal
                if not current == "terminal":
                    open_terminal()
                    current = "terminal"

            # this one will open up the computer settings
            if fingerUp == [0, 1, 1, 1, 1]:
                    # open settings
                if not current == "settings":
                    open_settings()
                    print(current)
                    current = "settings"

                # this one will center the cat and make it larger
                # if fingerUp == [1, 1, 1, 1, 1]:
                # make cat larger and center it

                # this will allow user to pick up the cat
                # if fingerUp == [1, 1, 0, 0, 0]:
                # pick up cat

                # this will allow the user to close the program
            # if fingerUp == [1, 0, 0, 0, 0]:
            #     print("destroy")
            #     cv2.destroyAllWindows()
            #     break

            if fingerUp == [0, 0, 0, 0, 0]:
                current = "empty"
        
        #current = ""

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break


if __name__ == '__main__': 
    main()
