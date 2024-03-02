# This will hold functions used for the User (hand recognition)

import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import tasks
from roboflow import Roboflow
import supervision as sv
from dotenv import load_dotenv
import os

# import json


# def hand_loop(video, current, detector):


# hands, img = detector.findHands(frame)

# cv2.rectangle(img, (0, 480), (300, 425), (0, 0, 0), -2)
# cv2.rectangle(img, (640, 480), (300, 425), (0, 0, 0), -2)

# if hands:
#     lmlist = hands[0]
#     fingerUp = detector.fingersUp(lmlist)

#     if current == "":
#         current = CLIENT.infer(frame, model_id="asl-alphabet-recognition/7")
#         print(current)
#         print(current["predictions"])
#         if len(current["predictions"]) > 0:
#             current = current["predictions"][0]
#             print(current)
#         else:
#             current = ""
# # this one will open default web browser
# if fingerUp == [0, 1, 0, 0, 0]:
#     # open web browser
#     if not current == "google":
#         tasks.open_google()
#         print(current)
#         current = "google"

# # this one will open notepad
# if fingerUp == [0, 1, 1, 0, 0]:
#     # open notepad
#     if not current == "notepad":
#         tasks.open_notepad()
#         print(current)
#         current = "notepad"

# # this one will open up the command prompt
# if fingerUp == [0, 1, 1, 1, 0]:
#     # open terminal
#     if not current == "terminal":
#         tasks.open_terminal()
#         current = "terminal"

# # this one will open up the computer settings
# if fingerUp == [0, 1, 1, 1, 1]:
#     # open settings
#     if not current == "settings":
#         tasks.open_settings()
#         print(current)
#         current = "settings"

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

#     if fingerUp == [0, 0, 0, 0, 0]:
#         current = "empty"
# return current


def main():
    rf = Roboflow(api_key=os.getenv('API_KEY'))
    project = rf.workspace().project("asl-alphabet-recognition")
    model = project.version(7).model

    video = cv2.VideoCapture(0)
    video.set(cv2.CAP_PROP_FRAME_WIDTH,320)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
    video.set(cv2.CAP_PROP_BUFFERSIZE, 2)
    while True:
        ret, frame = video.read()

        result = model.predict(frame, confidence=40, overlap=30).json()

        labels = [item["class"] for item in result["predictions"]]

        detections = sv.Detections.from_roboflow(result)

        label_annotator = sv.LabelAnnotator()
        box_annotator = sv.BoxAnnotator()

        annotated_image = box_annotator.annotate(scene=frame, detections=detections)
        annotated_image = label_annotator.annotate(
            scene=annotated_image, detections=detections, labels=labels
        )

        cv2.imshow("Hi, user!", annotated_image)

        # time.sleep(1 / 30)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


if __name__ == "__main__":
    load_dotenv()
    main()
