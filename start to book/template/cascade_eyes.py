import cv2


# 얼굴을 찾은 위치에서 눈 찾아야함 BUt 성능은 좋지않음
def detectEyes():
    src = cv2.imread("images/kids.png")

    if src is None:
        print("src None")
        return 

    classifier = cv2.CascadeClassifier("xml/haarcascade_eye.xml")

    if classifier.empty():
        print("classifier is None")
        return 


    eyes = classifier.detectMultiScale(src)

    for (x, y, w, h) in eyes:
        cv2.circle(src, (int(x + w/2), int(y + w / 2)), int(w / 2), (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow("src", src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

detectEyes()