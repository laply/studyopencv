# img pix  
import numpy as np
import cv2

img = cv2.imread('openCV\startOpenCV\image\Capture001.png')
px = img[340, 200]
print(px)

img.itemset((340, 200, 0), 100)

B = img.item(340, 200, 0)
G = img.item(340, 200, 1)
R = img.item(340, 200, 2)

BGR = [B, G, R]
print(B, G, R)

print(img.shape) # 이미지 해상도 및 컬러 채널 (height, width, color chennel num)
print(img.size)  # 이미지 사이즈 (byte)
print(img.dtype) # 이미지 데이터 타입

#image ROI 설정 
cv2.imshow('orignal', img)
subimg = img[300:400, 350:750]
cv2.imshow('cutting', subimg)

img[300 : 400, 0 : 400] = subimg

print(img.shape)
print(subimg.shape)

cv2.imshow('modified', img)

b, g, r = cv2.split(img)

cv2.imshow('blue channel', b)
cv2.imshow('green channel', g)
cv2.imshow('red channel', r)

cv2.waitKey(0)
cv2.destroyAllWindows()