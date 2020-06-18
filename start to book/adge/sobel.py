import numpy as np
import cv2


def sobelEdge():
    src = cv2.imread("images/cat.bmp", cv2.IMREAD_GRAYSCALE)

    if src is None:
        print("Can't open")
        return 

    # 각각의 방향에서 그레디언트를 구한다.
    # 소벨마스크를 이용하여 영상을 미분 Soble()

    dx = cv2.Sobel(src, cv2.CV_32FC1, 1, 0)
    dy = cv2.Sobel(src, cv2.CV_32FC1, 0, 1)

    fmag = cv2.magnitude(dx, dy) # sqrt(x^2, y^2)
    mag = np.uint8(np.clip(fmag, 0, 255))
    _, edge = cv2.threshold(mag, 150, 255, cv2.THRESH_BINARY)

    cv2.imshow("src", src)
    cv2.imshow("mag", mag)
    cv2.imshow("edge", edge)

    cv2.waitKey()
    cv2.destroyAllWindows()

sobelEdge()