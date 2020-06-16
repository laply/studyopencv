import sys
import numpy as np
import cv2


def on_mouse(event, x, y, flag, param):
    global cnt, srcPts
    if event == cv2.EVENT_LBUTTONDOWN:
        if cnt < 4 :
            srcPts[cnt, :] = np.array([x, y]).astype(np.float32)
            cnt += 1

            cv2.circle(src, (x, y), 5, (0, 0, 255), -1);
            cv2.imshow('src', src)

        if cnt == 4:
            w = 200
            h = 300

            dstPts = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]]).astype(np.float32)
            
            pers_mat = cv2.getPerspectiveTransform(srcPts, dstPts)

            dst = cv2.warpPerspective(src, pers_mat, (w, h))
            cv2.imshow('dst', dst)

cnt = 0
srcPts = np.zeros([4, 2], dtype=np.float32)
src = cv2.imread("images/card.bmp")

if src is None:
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('src')
cv2.setMouseCallback('src', on_mouse)

cv2.imshow('src', src)
cv2.waitKey(0)
cv2.destroyAllWindows()