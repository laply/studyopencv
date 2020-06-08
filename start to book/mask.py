import cv2 

def mask_copyTo():
    src = cv2.imread('airplane.bmp', cv2.IMREAD_COLOR)
    mask = cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
    dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

    if src is None or mask is None or dst is None:
        print('Image load failed!')
        return 

    cv2.copyTo(src, mask, dst)
    cv2.imshow('sum', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    mask_copyTo()