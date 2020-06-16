import cv2
import numpy as np

def affineTransform():
    src = cv2.imread("images/cat.bmp")

    if src is None :
        return 


    rows = src.shape[0]
    cols = src.shape[1]

    src_pts = np.array([[0, 0], [cols - 1, 0], [cols - 1, rows -1]]).astype(np.float32)
    dst_pts = np.array([[50, 50], [cols - 100, 100], [cols -50, rows -50]]).astype(np.float32)

    affineMat = cv2.getAffineTransform(src_pts, dst_pts)

    dst = cv2.warpAffine(src, affineMat, (0, 0))

    cv2.imshow("dst", dst)
    cv2.waitKey()
    cv2.destroyAllWindows()



def affineTranslation():
    src = cv2.imread("images/cat.bmp")

    if src is None :
        return 

    M = np.array([[1, 0, 150], [0, 1, 100]]).astype(np.float32)
    dst = cv2.warpAffine(src, M, (0, 0))

    cv2.imshow("dst", dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


def affineShear():
    src = cv2.imread("images/cat.bmp")
    if src is None:
        return 

    mx = 0.3 
    M  = np.array([[1, mx, 0], [0, 1, 0]]).astype(np.float32)

    dst = cv2.warpAffine(src, M, (int(src.shape[0]* mx + src.shape[1]), src.shape[0]))

    cv2.imshow("dst", dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

def affineScale():
    src = cv2.imread("images/cat.bmp")

    if src is None:
        return

    dst1 = cv2.resize(src, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
    dst2 = cv2.resize(src, (1920, 1280))
    dst3 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_CUBIC)
    dst4 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_LANCZOS4)

    cv2.imshow('dst1', dst1[500:900, 600:1000])
    cv2.imshow('dst2', dst2[500:900, 600:1000])
    cv2.imshow('dst3', dst3[500:900, 600:1000])
    cv2.imshow('dst4', dst4[500:900, 600:1000])
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    affineScale()
    # affineShear()
    # affineTranslation()
    # affineTranslation()