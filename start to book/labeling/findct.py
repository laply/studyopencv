import cv2
import random

def contoursHier():

    src = cv2.imread("images/pan.jpg", cv2.IMREAD_GRAYSCALE)

    if src is None:
        print(src)
        return 
    _, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    contours, hierarchy = cv2.findContours(src_bin, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

    
    for i in range(len(contours)):
        c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.drawContours(dst, contours, i, c, 2)

    cv2.imshow("src", src)
    cv2.imshow("src_bin", src_bin)
    cv2.imshow("dst", dst)

    cv2.waitKey(0);
    cv2.destroyAllWindows()

if __name__=="__main__":
    contoursHier()