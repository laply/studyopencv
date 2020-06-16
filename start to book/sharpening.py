import cv2

def unshape_mask():
    src = cv2.imread("images/cat.bmp", cv2.IMREAD_GRAYSCALE)

    if src is None:
        return

    cv2.imshow("src", src)

    for sigma in range(1, 6) :
        blurred = cv2.GaussianBlur(src, (0, 0), sigma)

        alpha = 1.0
        dst = cv2.addWeighted(src, 1 + alpha, blurred, -alpha, 0.0)

        cv2.imshow("dst", dst)
        cv2.waitKey()

    cv2.destroyAllWindows()

unshape_mask()