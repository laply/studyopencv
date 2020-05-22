# drawing 2 - use mouse

import numpy as np 
import cv2 
from random import shuffle

r = [i for i in range(256)]
g = [i for i in range(256)]
b = [i for i in range(256)]

def onMouse(event, x, y, flags, param):
    print("onMouse")
    if event == cv2.EVENT_LBUTTONDBLCLK:
        shuffle(r), shuffle(g), shuffle(b)
        cv2.circle(param, (x, y), 50, (r[233], g[41], b[25]), -1)

def mouseBrush():
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.namedWindow('paint')
    cv2.setMouseCallback('print', onMouse, param=img)
    print("onMouse2")
    while True:
        cv2.imshow('paint', img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    
    cv2.destroyAllWindows()

mouseBrush()
