# image burring

import numpy as np
import cv2

def bluring():
    img = cv2.imread('openCV/startOpenCV/image/test1.jpg')

    kernel = np.ones((5, 5), np.float32)/25
    # 5x5 배열 / 25 

    blur = cv2.filter2D(img, -1, kernel) 

    cv2.imshow('original', img)
    cv2.imshow('blur', blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

bluring()