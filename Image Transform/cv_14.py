# find 엣지 use img gradient 
# openCV Gradient filter (Sobel, Scharr, Laplacian)

# sobel and sharr Derivatives 

import numpy as np
import cv2
import matplotlib.pyplot as plt

def grad():
    img = cv2.imread('openCV/startOpenCV/image/test1.jpg', cv2.IMREAD_GRAYSCALE)

    laplacian = cv2.Laplacian(img, cv2.CV_64F)

    # cv2.Sobel(src(원본이미지), ddepth(이미지 데이터타입), dx(x방향 미분차수), dy(y방향 미분차수), Sobel 커널 크기)
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)

    plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
    plt.title('original'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
    plt.title('laplacian'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
    plt.title('sobel x'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
    plt.title('sobel y'), plt.xticks([]), plt.yticks([])

    plt.show()

grad()