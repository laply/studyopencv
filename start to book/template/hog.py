import cv2
import random

def main():
    cap = cv2.VideoCapture("Video/vtest.avi")

    if not cap.isOpened():
        return

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector() )

    while True:
        ret, frame = cap.read()
        if not ret :
            return 

        detected, _ = hog.detectMultiScale(frame)

        for (x, y, w, h) in detected:
            c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            cv2.rectangle(frame, (x, y), (x + w, y + h), c, 3)

        cv2.imshow("frame", frame)

        if cv2.waitKey(10) == 27:
            break


main()