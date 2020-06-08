import cv2


def conf():
    src = cv2.imread("cat.bmp", cv2.IMREAD_GRAYSCALE)

    if src is None:
        return

    b = 2.0
    d = 1/2
    Br = cv2.multiply(src, b)
    Dr = cv2.multiply(src, d)
    cv2.imshow("normal", src)
    cv2.imshow("*2.0", Br)
    cv2.imshow("/2", Dr)
    cv2.waitKey()
    cv2.destroyAllWindows()


def conf2():
    src = cv2.imread("cat.bmp", cv2.IMREAD_GRAYSCALE)

    if src is None:
        return
    
    alpha = 1.0

    dst = cv2.add(src, cv2.multiply(cv2.add(src, -128),alpha))
    
    cv2.imshow("useful", dst)
    cv2.imshow("base", src)
    cv2.waitKey()
    cv2.destroyAllWindows()

    

if __name__=="__main__":
    conf2()