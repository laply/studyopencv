# CLAHE -- 타일(8x8)별로 균일하게 콘트라베이스 적용하는 방법

import numpy as np
import cv2

def clahe():
    img = cv2.imread('openCV/startOpenCV/image/test5.png', cv2.IMREAD_GRAYSCALE)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    img2 = clahe.apply(img)

    res = np.hstack((img, img2))

    cv2.imshow('clahe', res)
    cv2.waitKey(0)
    cv2.imwrite('openCV/startOpenCV/image/clahe.jpg', res)
    cv2.destroyAllWindows()

clahe()