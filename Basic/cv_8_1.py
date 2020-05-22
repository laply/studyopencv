import numpy as np
import cv2

def onMouse(x):
    pass 

def imgBlending(imgfile1, imgfile2):
    img1 = cv2.imread(imgfile1)
    img2 = cv2.imread(imgfile2)

    cv2.namedWindow('ImgPane')
    cv2.createTrackbar('MIXING', 'imgPane', 0, 100, onMouse)
    mix = cv2.getTrackPos('MIXING', "ImgPane")

    while True:
        img = cv2.addWeighted(img1, float(100-mix)/100, img2, float(mix)/100, 0)
        cv2.imshow('imgPane', img)

        k = cv2.waitKey(1) & 0xFF

        if k == 27:
            break

        mix = cv2.getTrackbarPos('MIXING', 'ImgPane')
    cv2.detroyAllWidows()

imgBlending('a', 'b')