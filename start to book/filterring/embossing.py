import cv2
import numpy as np

def embossing():
    src = cv2.imread("images/cat.bmp", cv2.IMREAD_GRAYSCALE)

    if src is None:
        return

    data = np.array([[-1, -1, 0],
                    [-1, 0, 1],
                    [0, 1, 1]], np.float32)

    dst = cv2.filter2D(src, -1, data, delta=128)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    embossing()