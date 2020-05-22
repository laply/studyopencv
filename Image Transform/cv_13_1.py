# Opening // Closing -- 노이즈 제거 

# opening >> erosion and dialation
# closing >> dialation and erosion

import numpy as np
import cv2 

def morph():
    img1 = cv2.imread('openCV/startOpenCV/image/cv_13_1.png')

    kernel = np.ones((5, 5), np.uint8)

    opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, kernel)
    # 이미지 변형 operation  
    # cv2.MORPH_OPEN : Opening
    # cv2.MORPH_CLOSE : Closeing
    # cv2.MORPH_GRADINET : Dilation 이미지와 Erosion 이미지의 차이
    # cv2.MORPH_TOPHAT : 원본이미지와 opening 이미지의 차이
    # cv2.MORPH_BLACKHAT : closing 한 이미지와 원본 이미지의 차이를 나타냄 


    cv2.imshow('original', img1)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


morph()


def makeKernal() :
    M1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)) # 직사각형 커널
    M2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5)) # 타원형 커널 