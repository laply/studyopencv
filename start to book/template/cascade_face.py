import cv2

def detectFace():
    src = cv2.imread("images/face.jpg")

    if src is None:
        print("src None")
        return 

    classifier = cv2.CascadeClassifier("xml/haarcascade_frontalface_default.xml")

    if classifier.empty():
        print("classifier is None")
        return 


    faces = classifier.detectMultiScale(src)

    for (x, y, w, h) in faces:
        st1 = (x, y)
        st2 = (x+w, y+h)
        cv2.rectangle(src, st1, st2, (255, 0, 255), 2)

    cv2.imshow("src", src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

detectFace()