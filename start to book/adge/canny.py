import cv2

# 엣지 검출을 최적화 문제 관점으로 접근 
# 가우시안 필터링, 그레디언트 계산, 비최대 억제, 엣지 트레킹

def cannyEdge():
    src = cv2.imread("images/cat.bmp", cv2.IMREAD_GRAYSCALE)

    if src is None:
        print("Image can't load")
        return 

    dst1 = cv2.Canny(src, 50, 100)
    dst2 = cv2.Canny(src, 50 ,150)

    cv2.imshow("src", src)
    cv2.imshow("dst1", dst1)
    cv2.imshow("dst2", dst2)
    cv2.waitKey()
    cv2.destroyAllWindows()


cannyEdge()