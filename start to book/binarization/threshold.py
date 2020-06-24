import cv2 
# 전역 이진화


def on_threshold(pos):
    _, dst = cv2.threshold(src, pos, 255, cv2.THRESH_BINARY)
    cv2.imshow('dst', dst)

src = cv2.imread("images/neutrophils.png", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("None")

cv2.imshow('src', src)
cv2.namedWindow("dst")
cv2.createTrackbar("Threshold", 'dst', 0, 255, on_threshold)
cv2.setTrackbarPos("Threshold", 'dst', 128)

cv2.waitKey(0)
cv2.destroyAllWindows()
