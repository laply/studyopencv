# video 1
import numpy as np
import cv2

def showVideo():
    try :
        
        cap = cv2.VideoCapture("http://172.30.1.7:8891/?action=stream")
    except:
        return 


    cap.set(3, 480)
    cap.set(4, 320)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('video', gray)
        
        k = cv2.waitKey(1) & 0xFF
        
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

showVideo()
