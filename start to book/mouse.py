import cv2

def mouse():
    img = cv2.imread("images/cat.bmp")

    if img is None:
        return 

    cv2.namedWindow("Cat")
    cv2.setMouseCallback("Cat", on_mouse)
    cv2.imshow("Cat", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def on_mouse(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("L")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("R")



if __name__ == '__main__':
    mouse()