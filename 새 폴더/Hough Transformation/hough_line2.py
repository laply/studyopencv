# Probabilistic Hough Transformation Line

import numpy as np
import cv2

def hough(thr, minLineLength, maxLineGap):
    img = cv2.imread('openCV/startOpenCV/image/hough1.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(imgray, 50, 150, apertureSize=3)

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, thr, minLineLength, maxLineGap)

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow('ras', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

hough(100, 80, 5)