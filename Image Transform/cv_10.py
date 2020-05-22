# Thresholding 
# cv2.threshold
# 픽셀 문턱 값 보다 크면 

import numpy as np 
import cv2

img = cv2.imread('openCV\startOpenCV\image\Capture001.png')

ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)     # 픽셀 문턱 값 보다 크면 255 작으면 0
ret, thr2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV) # !(픽셀 문턱 값 보다 크면 255 작으면 0)
ret, thr3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)      # 픽셀 문턱 값 보다 크면 픽셀 문턱 값 작으면 그대로
ret, thr4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)     # 픽셀 문턱 값 보다 크면 픽셀 값 작으면 0
ret, thr5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV) # !(픽셀 문턱 값 보다 크면 그대로 작으면 그대로)

cv2.imshow('orignal', img)
cv2.imshow('THRESH_BINARY', thr1)
cv2.imshow('THRESH_BINARY_INV', thr2)
cv2.imshow('THRESH_TRUNC', thr3)
cv2.imshow('THRESH_TOZERO', thr4)
cv2.imshow('THRESH_TOZERO_INV', thr5)

cv2.waitKey(0)
cv2.destroyAllWindows()