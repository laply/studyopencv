import cv2
import numpy as np
import math


# 허프변환에 대한 기본지식만 갖고 가기

# 기본적인 허프 변환 직선 검출
def houghLines():
    src = cv2.imread("images/building.jpg", cv2.IMREAD_GRAYSCALE)

    if src is None:
        print ("Image load failes")
        return
    
    edge = cv2.Canny(src, 50, 150) # edge를 구한 다음 
    lines = cv2.HoughLines(edge, 1, math.pi / 180, 230) # 직선의 방정식 파라미터 p 와 th 정보를 line에 저장 
    dst = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR) 

    # 구한 값을 아용하여 에지 영상에 빨간색 직선을 그리기 위한 코드 
    for i in range(lines.shape[0]): 
        r = lines[i][0][0]
        t = lines[i][0][1]
        
        cos_t = math.cos(t)
        sin_t = math.sin(t)

        x = r * cos_t
        y = r * sin_t
        
        alpha = 1000

        pt1 = (int(x - alpha * sin_t), int(y + alpha * cos_t))
        pt2 = (int(x + alpha * sin_t), int(y - alpha * cos_t))
        cv2.line(dst, pt1, pt2, (0,0,255), 2, cv2.LINE_AA)

    cv2.imshow("src", src)
    cv2.imshow("dst", dst)

    cv2.waitKey()
    cv2.destroyAllWindows()


def houghLineSegments():
    src = cv2.imread("images/building.jpg", cv2.IMREAD_GRAYSCALE)

    if src is None:
        print ("Image load failes")
        return
    
    edge = cv2.Canny(src, 50, 150) # edge를 구한 다음 
    lines = cv2.HoughLinesP(edge, 1, math.pi / 180, 160, minLineLength=50, maxLineGap=5) #선분의 시작점과 끝점을 line에 저장 
    dst = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR) 

    # 구한 값을 아용하여 에지 영상에 빨간색 직선을 그리기 위한 코드 
    for i in range(lines.shape[0]): 
        pt1 = (lines[i][0][0], lines[i][0][1])
        pt2 = (lines[i][0][2], lines[i][0][3])
        cv2.line(dst, pt1, pt2, (0,0,255), 2, cv2.LINE_AA)

    cv2.imshow("src", src)
    cv2.imshow("dst", dst)

    cv2.waitKey()
    cv2.destroyAllWindows()

# 원 검출 3차원 파라미터 공간에서 축적 배열을 정의하고 사용 (시간이 많이 걸림)
# so openCV 에서는 일반적인 허프 변환이 아닌 허프 그래디언트 방법을 사용
def houghCircles():
    src = cv2.imread("images/one.jpg", cv2.IMREAD_GRAYSCALE)

    if src is None:
        print("None")
        return 

    blurred = cv2.blur(src, (3,3))

    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 50, param1=150, param2=30)
    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

    
    for i in range(circles.shape[1]):
        cx, cy, radius = circles[0][i]
        cv2.circle(dst, (cx, cy), radius, (0, 0, 255), 2, cv2.LINE_AA)


    cv2.imshow("src", src)
    cv2.imshow("dst", dst)

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    houghCircles()
    # houghLineSegments()

