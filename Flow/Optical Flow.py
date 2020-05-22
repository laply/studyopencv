# optical flow 
# 두 개의 연속된 비디오 프레임 사이에 이미지 객체의 가시적인 동작 패턴
# Optical Flow는 움직임을 통한 구조분석, 비디오 압축, video Stabilization (흔들림 영상 처리)

# openCV는 Lucas-Kanade 방법을 이용해 Optical Flow를 계산하는 함수 제공 
# cv2.calcOpticalFlowPyrLK()

# 비디오 이미지 추적 포인트를 결정하기 위해 cv2.goodFeatruesToTrack()을 이용
# 제대로 된 Optical Flow를 구현하려면 특성 포인트 들이 하나의 프레임이 아니라 특정 구간 마다 새롭게 검출해야함
import numpy as np
import cv2

termination = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)
feature_params = dict( maxCorners=200, qualityLevel=0.01, minDistance=7, blockSize=7 )
lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=termination)


class App:
    def __init__(self):
        self.track_len = 10
        self.detect_interval = 5
        self.tracks =[]
        self.cam = cv2.VideoCapture("http://172.30.1.7:8891/?action=stream")
        self.frame_idx = 0 
        self.blackscreen = False
        self.width = int(self.cam.get(3))
        self.height = int(self.cam.get(4))

    def run(self):
        while True:
            ret, frame = self.cam.read()
            if not ret:
                break
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            vis = frame.copy()
            if self.blackscreen:
                vis = np.zeros((self.height, self.width, 3), np.uint8)
            if len(self.tracks) > 0:
                img0, img1 = self.prev_gray, frame_gray
                p0 = np.float32([tr[-1] for tr in self.tracks]).reshape(-1, 1, 2)
                p1, st, err = cv2.calcOpticalFlowPyrLK(img0, img1, p0, None, **lk_params)
                p0r, st, err = cv2.calcOpticalFlowPyrLK(img1, img0, p1, None, **lk_params)
                d = abs(p0-p0r).reshape(-1, 2).max(-1)
                good = d < 1
                new_tracks = []
                for tr, (x, y), good_flag in zip(self.tracks, p1.reshape(-1, 2), good):
                    if not good_flag:
                        continue
                    tr.append((x, y))
                    if len(tr) > self.track_len:
                        del tr[0]
                    new_tracks.append(tr)
                    cv2.circle(vis, (x, y), 2, (0, 255, 0), -1)
                self.tracks = new_tracks
                cv2.polylines(vis, [np.int32(tr) for tr in self.tracks], False, (0, 255, 0))
            if self.frame_idx % self.detect_interval == 0:
                mask = np.zeros_like(frame_gray)
                mask[:] = 255
                for x, y in [np.int32(tr[-1]) for tr in self.tracks]:
                    cv2.circle(mask, (x,y), 5, 0, -1)
                p = cv2.goodFeaturesToTrack(frame_gray, mask=mask, **feature_params)
                if p is not None:
                    for x, y in np.float32(p).reshape(-1, 2):
                        self.tracks.append([(x, y)])
            self.frame_idx += 1
            self.prev_gray = frame_gray
            cv2.imshow('frame', vis)
            k = cv2.waitKey(30) & 0xFF
            if k == 27:
                break
            if k == ord('b'):
                self.blackscreen = not self.blackscreen
        self.cam.release()

App().run()
cv2.destroyAllWindows()
