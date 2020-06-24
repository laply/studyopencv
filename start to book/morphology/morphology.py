import cv2

src = cv2.imread('images/milkdrop.bmp', cv2.IMREAD_GRAYSCALE)

def erode():
    _, bin = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    dst1 = cv2.erode(bin, None)
    cv2.imshow('dst1', dst1)

def dilate():
    _, bin = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    dst2 = cv2.dilate(bin, None)
    cv2.imshow('dst2', dst2)

if (src is None) : 
    erode()
    dilate()
    cv2.waitKey()
    cv2.destroyAllWindows()


def open_close():
    _, bin = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    dst1 = cv2.morphologyEx(bin, cv2.MORPH_OPEN, None) # 침식 후 팽창 
    dst2 = cv2.morphologyEx(bin, cv2.MORPH_CLOSE, None) # 팽창 후 침식
    cv2.imshow('dst1', dst1)
    cv2.imshow('dst2', dst2)
    cv2.waitKey()
    cv2.destroyAllWindows()

if not (src is None) : 
    open_close()