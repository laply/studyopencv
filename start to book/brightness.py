import numpy as np
import cv2


def brightness1():
    img1 = cv2.imread("cat.bmp", cv2.IMREAD_GRAYSCALE)

    if img1 is None :
        return

    dst1 = cv2.add(img1, +100)
    dst2 = cv2.add(img1, -100)


    cv2.imshow("+100", dst1)
    cv2.imshow("normal", img1)
    cv2.imshow("-100", dst2)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    brightness1()