import numpy as np
import cv2


def shito():
    img = cv2.imread('openCV/image/corner.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(imgray, 100, 0.01, 30)
    corners = np.int0(corners)

    for i in corners:
        x, y = i.ravel()
        cv2.circle(img, (x, y), 3, 255, -1)

    cv2.imshow('shito', img)
    cv2.waitKey()
    cv2.destroyAllWindows()

shito()