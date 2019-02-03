#coding=utf-8
'''
    背景消除，移动物体检测
    轮廓检测
    基于背景的运动检测
'''
import numpy as np
import cv2
import time
import imutils
import argparse
import datetime
from imutils.video import VideoStream

# cap = cv2.VideoCapture(0)
# cap.set(3,320)
# cap.set(4,240)
vs = VideoStream(src=0).start()


ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())

firstFrame = None
while(True):
    # ret,frame = cap.read()
    frame = vs.read()
    img = frame


    # 灰度处理
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    #获取第一帧为背景
    if firstFrame is None:
        firstFrame = gray

    print(firstFrame)
    frameDelta = cv2.absdiff(firstFrame, gray)
    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c) < args["min_area"]*2:
			continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Occupied"




    text = "opject"
    cv2.putText(frame, "Iterm: {}".format(text), (10, 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, datetime.datetime.now().strftime("%Y-%M-%D %H:%M:%S"),
		(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    # cv2.imshow('gray',gray)
    # cv2.imshow('frameDelta',frameDelta)
    cv2.imshow('thresh',thresh)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# cap.release()
# cv2.destroyAllWindows()
vs.stop() if args.get("video", None) is None else vs.release()
cv2.destroyAllWindows()




