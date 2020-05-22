import numpy as np 
import cv2

def thresholding():

    img = cv2.imread('openCV\startOpenCV\image\Capture001.png', cv2.IMREAD_GRAYSCALE) 
    # GRAYSCALE로 변환해서 읽지 않음 에러 

    ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    thr2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 5)
    thr3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
    title = ['original', 'Global Threasholding(v=127)', 'Adaptive MEAN', 'Adaptive GAUSSIAN' ]
    imges = [img, thr1, thr2, thr3]


    for i in range(4):
        cv2.imshow(title[i], imges[i])

    cv2.waitKey(0)
    cv2.destroyAllWindows()

thresholding()