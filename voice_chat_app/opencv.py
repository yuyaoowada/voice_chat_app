import time

import cv2 as cv


def video_playback():
    """Video playback by OpenCV"""
    cap = cv.VideoCapture('docs/zundamon.mp4')
    try:
        # while cap.isOpened():
        ret, img = cap.read()

        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            # break
        #     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        while True:
            cv.imshow('Video', img)
            if cv.waitKey(1) == ord('q'):
                break
    except cv.error as e:
        print(f"OpenCV Error: {e}")
    finally:
        cap.release()
        cv.destroyAllWindows()
        print(f"Destroyed all windows")
