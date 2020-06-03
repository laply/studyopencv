# histogram 균일화 -- 동일한 조명 조건을 만들어주는 유용한도구

import numpy as np
import cv2

def histogram():
    img0 = cv2.imread('openCV/startOpenCV/image/test1.jpg', cv2.IMREAD_GRAYSCALE)
    img = cv2.imread('openCV/startOpenCV/image/test1.jpg', cv2.IMREAD_GRAYSCALE)

    hist, bins = np.histogram(img.ravel(), 256, [0, 256])
    cdf = hist.cumsum()

    cdf_m = np.ma.masked_equal(cdf, 0)
    print(cdf_m)
    cdf_m = (cdf_m - cdf_m.min())*255 / (cdf_m.max() - cdf_m.min()) # 히스토그램 균일화 방정식
    cdf = np.ma.filled(cdf_m, 0).astype('uint8') # 마스크 처리 부분 재 변환 

    img2 = cdf[img]
    
    cv2.imshow('Histogram Equalization before', img0)
    cv2.imshow('Histogram Equalization', img2)
    cv2.waitKey(0)

    cv2.imwrite('openCV/startOpenCV/image/test4_change.jpg', img2)
    cv2.destroyAllWindows()


histogram()