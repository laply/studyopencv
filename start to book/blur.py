import numpy as np
import cv2


def blurring():
    src = cv2.imread("images/cat.bmp")
    
    if src is None:
        return 
    
    # blur = np.array([1, 1, 1], [1, 1, 1], [1, 1, 1], np.float32)

    for i in (3, 5, 7):
        dst = cv2.blur(src, (i, i))

        txt = ": %dx%d" % (i, i)

        cv2.putText(dst, txt, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                   1.0, 255, 1, cv2.LINE_AA)
        cv2.imshow('dst', dst)
        cv2.waitKey()
    cv2.destroyAllWindows()

def gaussian():
    src = cv2.imread("images/cat.bmp")
    

    if src is None :
        return 

    
    for i in range(1, 6):
       dst = cv2.GaussianBlur(src, (0, 0), i) 
       txt = "sigma : %d" % i


       cv2.putText(dst, txt, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 255, 1)

       cv2.imshow("dst", dst)
       cv2.waitKey()

    cv2.destroyAllWindows()

def gaussian_video():

    cap = cv2.VideoCapture('http://115.20.144.97:11092/?action=stream')

    if not cap.isOpened():
        print("camera open failed")
        return 

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        dst = cv2.GaussianBlur(frame, (0, 0), 3) 
        
        cv2.imshow('dst', dst)
        if cv2.waitKey(10) == 27:
            break

    cv2.destroyAllWindows()

    

if __name__ == "__main__" :
    #blurring()
    gaussian_video()