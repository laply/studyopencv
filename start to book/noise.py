import cv2


def noise_gaussian() :
    src = cv2.imread("images/cat.bmp")
    
    if src is None:
        return

    for (stddev )