# Erosion(이미지 침식), Dilation(이미지 팽창) - img 형태 변환 

# Erosion -- 배경이미지로 부터 안쪽으로 이동 
# Dilation -- 배경 이미지로 부터 밖으로 이동

import numpy as np
import cv2

def morph():
    img = cv2.imread('openCV/startOpenCV/image/images.png')

    kernal = np.ones((3, 3), np.uint8)

    erosion = cv2.erode(img, kernal, iterations = 1)
    dilation = cv2.dilate(img, kernal, iterations = 1)

    cv2.imshow('original', img)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



morph()
