#coding=utf-8
'''
    树莓派上移动人体检测
	添加日志模块
'''
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

import numpy as np
import cv2
import logging


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='log_background.log', level=logging.DEBUG, format=LOG_FORMAT)


camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))
time.sleep(0.1)

# 算法代码
fgbg = cv2.createBackgroundSubtractorMOG2()

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    image = cv2.flip(image,0)



    
    # 算法代码
    fgmask = fgbg.apply(image)
    num = fgmask.mean()
    print(num)
    if num > 1:
        print('检测到有人活动')
    # logging.info(111111)
    # for i in fgmask:
    #     logging.info(i)

    cv2.imshow('image',image)
    cv2.imshow('mask',fgmask)




    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    if key == ord("q"):
        break    


