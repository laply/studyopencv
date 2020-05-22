# 이미지의 크기가 달라지더라도 이미지의 특징적인 부분을 검출
# 스케일 불변인 키포인트를 추출하고, 추출한 키 포인트들의 desriptor를 계산

# 1. Scale-space Exterma Detection 스케일-공간 극값 검출
# 가우시안 필터 후 라플라시안 (Laplacian of Gaussian : LoG) 팔터를 적용하면 
# 이미지에서 다양한 크기의 방을 모양의 이미지를 검출한다.
# LoG는 다소 시간이 소요되기 때문에 가우시안 피라미드 이미지의 차를 이용한다 (Difference of Gaussian : DoG)
# DoG를 찾으면 이미지에서 스케일 - 공간 좌표상 극값을 찾는다. 만약 극값이 있으면 이를 잠재적 키포인트라 한다. (Potential Keypoint)

# 2. Keypoint Localiztion 키포인트 지역화 
# 이미지에서 잠재적 키포인틀의 위치를 모두 찾았으면 정확한 결과를 위해 잠재적 키포인트들의 정제과정을 거쳐 키포인트를 추철한다. 
# 테일러 전게를 이용 

# 3. Orientation Assignment 방향 할당하기 
# 방향성-불변이 되도록 방향을 할당한다. (회전 하더라도 이미지의 특징 보존)

# 4. KeyPoint Descriptor 키포인트 디스크립터 계산하기
# 5. Keypoint Matching  

import numpy as np
import cv2

def SIFT():
    img = cv2.imread('openCV/image/bf.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2, img3 = None, None

    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(imgray, None)

    img2 = cv2.drawKeypoints(imgray, kp, img2)
    img3 = cv2.drawKeypoints(imgray, kp, img3, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imshow('SIFT1', img2)
    cv2.imshow('SIFT2', img3)
    cv2.waitkey(0)
    cv2.destroyAllWindows()

SIFT()