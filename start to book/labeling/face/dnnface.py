import cv2

model = "model/res10_300x300_ssd_iter_140000_fp16.caffemodel"
config = "model/deploy.prototxt"

def main():
    cap = cv2.VideoCapture('http://115.20.144.97:11092/?action=stream')

    if not cap.isOpened():
        print("cap")
        return 

    net = cv2.dnn.readNet(model, config)

    if net.empty():
        print("net")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("ret")
            return


        blob = cv2.dnn.blobFromImage(frame, 1, (300, 300), (104, 177, 123))
        net.setInput(blob)
        detect = net.forward()

        (h, w) = frame.shape[:2]
        detect = detect[0, 0, :, :]

        for i in range(detect.shape[0]) :
            confidence = detect[i, 2]
            if confidence < 0.5:
                break

            x1 = int(detect[i, 3] * w)
            y1 = int(detect[i, 4] * h)
            x2 = int(detect[i, 5] * w)
            y2 = int(detect[i, 6] * h)

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0))

        cv2.imshow("frame", frame)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()

main()
