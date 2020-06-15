import cv2
import numpy as np

src = cv2.imread("images/cat.bmp", cv2.IMREAD_GRAYSCALE)

def noiseGaussian():

    if src is None:
        print("None")
        return

    cv2.imshow("src", src)

    for stb in range(1, 4):
        noise = np.zeros(src.shape, np.int32)
        cv2.randn(noise, 0, stb*10)

        dst = cv2.add(src, noise,dtype=cv2.CV_8UC1)

        desc = "stddev = %d" % stb*10
        cv2.imshow("dst", dst)
        cv2.waitKey()        
    cv2.destroyAllWindows()

noiseGaussian()