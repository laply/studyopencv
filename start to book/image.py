import numpy as np
import cv2

def func1():
    img1 = cv2.imread('cat.bmp')
    img2 = img1[120:360, 220:560]
    img1[120:360, 220:560] = ~img2
    
    if img1 is None:
        print('Image load failed!')
        return

    print('type(img1):', type(img1))
    print('img1.shape:', img1.shape)

    if len(img1.shape) == 2: # GRAY
        print('img1 is a grayscale image')
    elif len(img1.shape) == 3: # RGB
        print('img1 is a truecolor image')

    cv2.imshow('img1', img1)

    cv2.imshow('img2', img2)
    cv2.waitKey()
    cv2.destroyAllWindows()


func1()