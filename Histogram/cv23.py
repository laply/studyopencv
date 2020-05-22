# 이미지의 콘트라스트(Contrast), 밝기 (Brightness), 색감 분포 등과 같은 이미지의 특성에 대해 감을 잡게 해줌 

import numpy as np 
import cv2
import matplotlib.pyplot as plt 

def histogram():
    img2 = cv2.imread('openCV/startOpenCV/image/test1.jpg')
    img1 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # OpenCV 함수를 통한 히스토그램
    hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
    # numpy를 이용한 히스토그램
    hist2, bins = np.histogram(img1.ravel(), 256, [0, 256])
    # 1-D 히스토그램 
    hist3 = np.bincount(img1.ravel(), minlength=256)

    plt.hist(img1.ravel(), 256, [0, 256])

    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        hist = cv2.calcHist([img2], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])

    plt.show()

histogram()