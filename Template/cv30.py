# template matching 
# 이미지에서 특정 객체를 찾는 방법

import numpy as np
import cv2
import matplotlib.pyplot as plt

def tempMatching():
    img = cv2.imread('openCV/startOpenCV/image/test1.jpg', cv2.IMREAD_GRAYSCALE)
    img_2 = img.copy()

    template = cv2.imread('openCV/startOpenCV/image/test1_1.jpg', cv2.IMREAD_GRAYSCALE )
    w, h = template.shape[::-1]

    methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    for meth in methods:
        img1 = img_2.copy()
        method = eval(meth)

        try :
            res = cv2.matchTemplate(img1, template, method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        except:
            print('오류', meth)
            continue

        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else :
            top_left = max_loc 


        bottom_right = (top_left[0]+2, top_left[1]+h)
        cv2.rectangle(img1, top_left, bottom_right, 255, 2)

        plt.subplot(121), plt.imshow(res, cmap = 'gray')
        plt.title('matching result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(res, cmap = 'gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)

        plt.show()
    
tempMatching()