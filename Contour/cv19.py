# convex Hull (볼록체) == Contour의 오목한부분을 체크 이를 보정함  // 오목한 부분이 없는 선 

import numpy as np
import cv2

img = cv2.imread('openCV/startOpenCV/image/test3.png')
img1 = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thr = cv2.threshold(imgray, 127, 255, 0)
contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

def convex():
    cnt = contours[0]
    cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)

    check = cv2.isContourConvex(cnt) # Convex Hull 인지 체크 
    
    if not check:
        hull = cv2.convexHull(cnt)
        cv2.drawContours(img1, [hull], 0, (0, 255, 0), 3)
        cv2.imshow('convexhull', img1)
    
    cv2.imshow('contour', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# convex()

def convex1():
    cnt = contours[0]
    
    x, y, w, h = cv2.boundingRect(cnt) # bounding ract 표면 사각형 x, y, w, h 
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)

    rect = cv2.minAreaRect(cnt) # 가장 작은 면적의 직사각형 
    box = cv2.boxPoints(rect) # 꼭지점 좌표
    box = np.int0(box)

    cv2.drawContours(img, [box], 0, (0, 255, 0), 3)

    cv2.imshow('retangle', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# convex1()


def convex2():
    rows, cols = img.shape[:2]
    cnt = contours[0]

    (x, y), r = cv2.minEnclosingCircle(cnt)
    center = (int(x), int(y))
    r = int(r)

    cv2.circle(img, center, r, (255, 0, 0), 3)

    ellipse = cv2.fitEllipse(cnt)
    cv2.ellipse(img, ellipse, (0, 255, 0), 3)

    cv2.imshow('etc', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

convex2()
