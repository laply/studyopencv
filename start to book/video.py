import numpy as np
import cv2

cap = cv2.VideoCapture('http://115.20.144.97:11092/?action=stream')



def camera_in():

    if not cap.isOpened():
        print("camera open failed")
        return 

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        inversed = ~frame
        
        cv2.imshow('frame', frame)
        cv2.imshow('inversed', inversed)

        if cv2.waitKey(10) == 27:
            break

    cv2.destroyAllWindows()


def camera_in_video_out():
    if not cap.isOpened():
        print("camera open failed")
        return 

    w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)


    fourcc = cv2.VideoWriter_fourcc(*'DIVX') # *'DIVX' == 'D', 'I', 'V', 'X'
    delay = round(1000 / fps)

    outputVideo = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        inversed = ~frame

        outputVideo.write(inversed)
        
        cv2.imshow('frame', frame)
        cv2.imshow('inversed', inversed)

        if cv2.waitKey(delay) == 27:
            break

    cv2.destroyAllWindows()



if __name__ == '__main__':
    camera_in_video_out()