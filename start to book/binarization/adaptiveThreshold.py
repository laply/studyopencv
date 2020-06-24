import cv2 
# 전역 이진화


def on_threshold(pos):

    bsize = pos
    if bsize % 2 == 0 :
        bsize -= 1
    if bsize < 3 :
        bsize = 3


    # 각 픽셀 주변의 blocksize x blocksize 영역에서 평균을 구하고 
    # 평균에서 상수 c를 뺀 값을 해당 픽셀의 임계값으로 사용한다.
    dst = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, bsize, 5)
    cv2.imshow('dst', dst)

src = cv2.imread("images/sudoku.jpg", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("None")

cv2.imshow('src', src)
cv2.namedWindow("dst")
cv2.createTrackbar("Threshold", 'dst', 0, 200, on_threshold)
cv2.setTrackbarPos("Threshold", 'dst', 128)

cv2.waitKey(0)
cv2.destroyAllWindows()

