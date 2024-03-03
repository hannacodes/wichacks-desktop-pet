import cv2
from cvzone.HandTrackingModule import HandDetector
import mediapipe as mp
import math

class detector():
    def __init__(self, mode = False, maxHands = 1, detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]

    def findHand(self, img, draw = True):
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results -= self.hands.process(rgb)

        if self.results.multi_hand:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

            return img
    
    def findPos(self, img, handNumber = 0, draw = True):
        x = []
        y = []
        box = []
        self.lmlist = []
        if self.results.multi_hand_landmarks:
            hand = self.multi_hand_landmarks[handNumber]
            for id, lm in enumerate(hand.landmark):
                h, w, d = img.shape
                dx, dy = int(lm.x * w), int(lm.y * h)
                x.append(dx)
                y.append(dy)
                self.lmlist.append([id, dx, dy])
                if draw:
                    cv2.circle(img, (dx, dy), 5, (255, 0, 255), cv2.FILLED)

                xmin, xmax = min(x), max(x)
                ymin, ymax = min(y), max(y)
                box = xmin, ymin, xmax, ymax
                
            if draw:
                cv2.rectangle(img, (xmin - 20, ymin - 20), (xmax + 20, ymax + 20), (0, 255, 0), 2)

        return self.lmlist, box
    
    def fingerDetect(self):
        fingers = []

        if self.lmlist[self.tipIds[0]][1] > self.lmlist[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 5):
            if self.lmlist[self.tipIds[id]][2] > self.lmlist[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers
    
    def findDistance(self, p1, p2, img, draw = True, r = 15, t = 3):
        x1, y1 = self.lmlist[p1][1:]
        x2, y2 = self.lmlist[p2][1:]
        dx, dy = (x1 + x2) // 2, (y1 + y2) // 2

        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), t)
            cv2.line(img, (x1, y1), r, (255, 0, 255), cv2.FILLED)
            cv2.line(img, (x2, y2), r, (255, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), r, (255, 0, 255), cv2.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)

        return length, img, [x1, x2, y1, y2, dx, dy]

def main():
    video = cv2.VideoCapture(0)
    detector = HandDetector()

    while True:
        success, img = video.read()
        img = detector.findHands(img)
        lmlist, box = detector.findPos(img)
        if len(lmlist) != 0:
            print(lmlist[4])

        cv2.imshow("Hi, user!", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


if __name__ == '__main__':
    main()