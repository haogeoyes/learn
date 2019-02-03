#coding=utf-8
'''
    树莓派上人脸检测
	添加日志模块
'''
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

import numpy as np
import cv2
import logging
import datetime


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT)

# logging.debug("This is a debug log.")
# logging.info("This is a info log.")
# logging.warning("This is a warning log.")
# logging.error("This is a error log.")
# logging.critical("This is a critical log.")

camera = PiCamera()
# camera.resolution = (640, 480)
camera.resolution = (320, 240)
camera.framerate = 32
# rawCapture = PiRGBArray(camera, size=(640, 480))
rawCapture = PiRGBArray(camera, size=(320, 240))
time.sleep(0.1)

# 人脸识别
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# frame = cv2.flip(frame,0)
	image = frame.array
	image = cv2.flip(image,0)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = image[y:y+h, x:x+w]

		timeNowFile = 'img/%s.jpg'%datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")
		timeNowFileMin = 'img/%s_min.jpg'%datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")
		cv2.imwrite(timeNowFile, image)
		cv2.imwrite(timeNowFileMin, roi_color)

		eyes = eye_cascade.detectMultiScale(roi_gray)

		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	# cv2.line(image,(0,100),(1000,100),(255,0,0),5)
	# if len(faces) != 0:
	# 	logging.info("检测到人脸")
	# 	timeNowFile = 'img/%s.jpg'%datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")
	# 	timeNowFileMin = 'img/%s_min.jpg'%datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")
	# 	cv2.imwrite(timeNowFile, image)
	# 	cv2.imwrite(timeNowFileMin, roi_color)


	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF
	rawCapture.truncate(0)
	if key == ord("q"):
		break    


