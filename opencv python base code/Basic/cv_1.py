# image lode 1

import numpy as np
import cv2

imgfile = './image/model.png'

def showImage():
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR)
    # cv2.IMREAD_COLOR = color image
    # cv2.IMREAD_GRAYSCALE = bw image
    # cv2.IMREAD_UNCHANGED = add Alpha-chennel

    cv2.imshow('model', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def showImage2(): # window size 
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR)

    cv2.namedWindow('model', cv2.WINDOW_NORMAL)
    cv2.imshow('model', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def showImage3():
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR)
    cv2.imshow('model', img)

    # key board data enter 
    k = cv2.waitKey(0) & 0xFF

    if k == 27:
        cv2.destoryAllWindow()
    elif k == ord('c'): # if c == copy
        cv2.imwrite('image/model_copy.jpg', img)
        cv2.destroyAllWindows()

showImage3()