# Contour의 특징 
# 면적, 둘레 길이, 폐곡선 시 중심 

#image moment 
# -- 객체의 무게중심, 객체의 면적과 같은 특성을 계산할때 유용

# 공간 모멘트 (spatial Moments)
# 중심 모멘트 (Centeral)
# 평준화 된 중심 모먼트 (Central Normalized Moments)
import numpy as np
import cv2

img = cv2.imread('openCV/startOpenCV/image/test2.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thr = cv2.threshold(imgray, 127, 255, 0)
contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

def moment(): # 무게중심의 x, t 좌표를 구하는 식


    contour = contours[0]
    mmt = cv2.moments(contour)

    for key, val in mmt.items():
        print('%s:\t%.5f' %(key, val))

    cx = int(mmt['m10']/mmt['m00'])
    cy = int(mmt['m01']/mmt['m00'])

    print(cx, cy)

moment()

# Contour Arear -둘러 싸인 부분의 면적 // Contour Perimeter -호의 길이
def contour():
    cnt = contours[0]
    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt, True)
    cv2.drawContours(img, [cnt], 0, (255, 255, 0), 3)

    print('contour 면적: ', area )
    print('contour 길이: ', perimeter)

    cv2.imshow('contour', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
contour()
    
# 찢겨진 사각형 복원 
def  contour2():
    cnt = contours[0]

    epsilon1 = 0.01*cv2.arcLength(cnt, True)
    epsilon2 = 0.1*cv2.arcLength(cnt, True)

    approx1 = cv2.approxPolyDP(cnt, epsilon1, True) 
    # 인자로 주어진 곡선 또는 다각형을 epsilon 값에 따라 꼭지점 수를 줄여 새로운 곡선이나 다각형 생성하여 리턴 
    approx2 = cv2.approxPolyDP(cnt, epsilon2, True)
    img1 = cv2.imread('openCV/startOpenCV/image/test2.png')
    img2 = cv2.imread('openCV/startOpenCV/image/test2.png')
    cv2.drawContours(img1, [approx1], 0, (255, 255, 0), 3)
    cv2.drawContours(img2, [approx2], 0, (255, 255, 0), 3)
    
    cv2.imshow('approx1', img1)
    cv2.imshow('approx2', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

contour2()
