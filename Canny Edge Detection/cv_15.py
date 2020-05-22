# canny Edge Detection -- 엣지 찾기 알고리즘 
# noise Reduction -> find Gradient high part -> make other fixel to 0 

import numpy as np 
import cv2
import matplotlib.pyplot as plt 

def canny():
    img = cv2.imread('openCV/startOpenCV/image/test1.jpg', cv2.IMREAD_GRAYSCALE)

    # cv2.Canny(src, min thresholding value, max thresholding value)
    edge1 = cv2.Canny(img, 50, 200)
    edge2 = cv2.Canny(img, 100, 200)
    edge3 = cv2.Canny(img, 170, 200)


    cv2.imshow('original', img)
    cv2.imshow('Canny Edge1', edge1)
    cv2.imshow('Canny Edge2', edge2)
    cv2.imshow('Canny Edge3', edge3)


    cv2.waitKey(0)
    cv2.destroyAllWindows()

canny()