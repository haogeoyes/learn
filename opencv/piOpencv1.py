#coding=utf-8
'''
    树莓派上显示视频
'''
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

import numpy as np
import cv2

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array
    cv2.line(image,(0,100),(511,100),(255,0,0),5)
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF
	rawCapture.truncate(0)
	if key == ord("q"):
		break    


