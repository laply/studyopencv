import numpy as np
import cv2

def FAST():
    img = cv2.imread('openCV/image/corner.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img2, img3 = None, None

    fast = cv2.FastFeatureDetector_create(20)
    kp = fast.detect(img, None)
    img2 = cv2.drawKeypoints(img, kp, img2, (255, 0, 0))
    cv2.imshow('FAST1', img2)

    fast.setNonmaxSuppression(0)
    kp = fast.detect(img, None)
    img3 = cv2.drawKeypoints(img, kp, img3, (255, 0, 0))
    cv2.imshow('FAST2', img3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

FAST()