import cv2
import numpy as np

def setLabel(img, pts, label):
    (x, y, h, w) = cv2.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x + h, y + w)
    cv2.rectangle(img, pt1, pt2, (0,0,255), 1)
    cv2.putText(img, label, pt1, cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))

def polygon():
    src = cv2.imread("images/pan.jpg", cv2.IMREAD_COLOR)

    if src is None:
        print("None")
        return

    gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    _, bin_img = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for i in contours:
        if cv2.contourArea(i) < 400:
            continue

        approx = cv2.approxPolyDP(i, cv2.arcLength(i, True)*0.02, True)

        vtc = len(approx)

        if vtc == 3:
            setLabel(src, i, "TRI")
        elif vtc == 4:
            setLabel(src, i, "RECT")
        elif vtc > 4: 
            length = cv2.arcLength(i, True)
            area = cv2.contourArea(i)
            ratio = 4. * np.pi * area / (length * length)

            if ratio > 0.8 :
                setLabel(src, i, "CIR")

    cv2.imshow("bin_img", bin_img)
    cv2.imshow("src", src)
    cv2.waitKey(0)
    return 0

polygon()
