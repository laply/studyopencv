import numpy as np
import cv2

oldx, oldy = -1, -1
img = None
def on_mouse(event, x, y, flags, _):
    global oldx, oldy, img
    
    if(event == cv2.EVENT_LBUTTONDOWN):
        oldx, oldy = x, y
    elif (event == cv2.EVENT_LBUTTONUP):
        oldx, oldy = -1, -1
    elif ((event == cv2.EVENT_MOUSEMOVE) and (flags and cv2.EVENT_FLAG_LBUTTON)):
        cv2.line(img, (oldx, oldy), (x, y), (255, 255, 255), 40, cv2.LINE_AA, 0)

        oldx, oldy = x, y
        cv2.imshow("img", img)


def setDatanTrainKnn():
    digit = cv2.imread("images/digits.png", cv2.IMREAD_GRAYSCALE)
    if digit is None:
        return

    h, w = digit.shape[:2]

    cells =[np.hsplit(row, w//20) for row in np.vsplit(digit, h//20)]
    cells = np.array(cells)
    train_images = cells.reshape(-1, 400).astype(np.float32)
    train_lables = np.repeat(np.arange(10), len(train_images)/10)

    knn = cv2.ml_KNearest.create()
    knn.train(train_images, cv2.ml.ROW_SAMPLE, train_lables)

    return knn

 
def main():
    global img
    knn = setDatanTrainKnn()

    if knn is None :
        return 

    img = np.zeros((400, 400), np.uint8)

    cv2.imshow("img", img)
    cv2.setMouseCallback("img", on_mouse)


    while(True):
        c = cv2.waitKey()

        if c == 27:
            break
        elif c == ord(' '):
            img_resize = cv2.resize(img, (20,20), interpolation=cv2.INTER_AREA)
    
            img_flatten = img_resize.reshape(-1, 400).astype(np.float32)

            ret, res, _, _  = knn.findNearest(img_flatten, 5)

            print(int(res[0, 0]))


        img.fill(0)
        cv2.imshow('img', img)

    cv2.destroyAllWindows()

if __name__ =="__main__":
    main()