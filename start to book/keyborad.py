import cv2


img = cv2.imread("cat.bmp", cv2.IMREAD_GRAYSCALE)

cv2.namedWindow("cat")
cv2.imshow("cat", img)


while True:
    if cv2.waitKey() == 27:
        break
    elif cv2.waitKey() == 'i':
        img = ~img
        cv2.imshow("cat", img)


cv2.destroyWindow("cat")