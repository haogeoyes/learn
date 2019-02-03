#coding=utf-8
'''
    树莓派上蓝色物体追踪
	添加日志模块
'''
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

import numpy as np
import cv2
import logging


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='log_blue.log', level=logging.DEBUG, format=LOG_FORMAT)


camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))
time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    image = cv2.flip(image,0)
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    #蓝色阀值
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    #掩模
    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    #运算
    res = cv2.bitwise_and(image,image,mask=mask)
    cv2.imshow('image',image)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    if key == ord("q"):
        break    


