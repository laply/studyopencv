import numpy as np
import cv2

def onMouse(x):
    pass

def bluring():
    img = cv2.imread('openCV/startOpenCV/image/test1.jpg')

    cv2.namedWindow('BlurPane')
    cv2.createTrackbar('BLUR_MODE', 'BlurPane', 0, 3, onMouse)
    cv2.createTrackbar('Blur', 'BlurPane', 0, 5, onMouse)

    mode = cv2.getTrackbarPos('BLUR_MODE', 'BlurPane')
    val = cv2.getTrackbarPos('Blur', 'BlurPane')

    while True:
        val = val*2 + 1

        try :
            if mode == 0:
                blur = cv2.blur(img, (val, val))
            elif mode == 1:
                blur = cv2.GaussianBlur(img, (val, val), 0)
                # 이미지의 가우스 노이즈 제거 효과
            elif mode == 2:
                blur = cv2.medianBlur(img, val)
                # 소금-후추 노이즈를 제거하는데 효과적
            elif mode == 3:
                blur = cv2.bilateralFilter(img, val, 75, 75)
                # etc -- bilateralFilter()
                # edge를 보존하고 표면의 질감을 제거 
            else:
                break

            cv2.imshow('BlurPane', blur)
        except:
            break

        k = cv2.waitKey(1) & 0xFF
        
        if k == 27:
            break
        mode = cv2.getTrackbarPos('BLUR_MODE', 'BlurPane')
        val = cv2.getTrackbarPos('Blur', 'BlurPane')

    cv2.destroyAllWindows()

bluring()