#coding=utf-8
'''
    树莓派上人脸检测
	添加日志模块
	舵机
'''



from picamera.array import PiRGBArray
from picamera import PiCamera
import time

import numpy as np
import cv2
import logging
import datetime



from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

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



 
def setServoAngle(servo, angle):
# def setServoAngle(operation):
# 	operation = [[17,0],[18,0]]
	# for i in operation:
	# 	servo = i[]
	# servo 引脚
	# angle 弧度 0-180度
    # GPIO.setup(servo, GPIO.OUT)
    pwm = GPIO.PWM(servo, 50)
    pwm.start(8)
    dutyCycle = angle / 18. + 3.
    pwm.ChangeDutyCycle(dutyCycle)
    sleep(2)
    pwm.stop()



def change(img,xy,start,startUp):
    print(start,startUp)
    x = int(width/2)
    y = int(height/2)
    cv2.circle(img,(x,y),3,(0,0,255),5)
    # print(x,y)
    cx,cy = xy
    w = x-cx
    h = y-cy
    # 需要移动的角度计算 换面换算角度是60度
    k = width/60
    # 需要移动的弧度
    radian = int(abs(w)/k)
    radianUp = int(abs(h)/k)
    if w > 0 and h > 0:
        start = start - radian
        startUp = startUp - radianUp
    else:
        start = start + radian
        startUp = startUp + radianUp
    print('左右弧度',start)
    print('高低弧度',startUp)
	# setServoAngle(pin,start)
	# setServoAngle(pinUp,startUp)
    # if radian > 0:
    # if radian > 10:
        # setServoAngle(pin,start)
        # setServoAngle(pinUp,startUp)
    


pin = 18
pinUp = 17
GPIO.setup(pin, GPIO.OUT)
GPIO.setup(pinUp, GPIO.OUT)

# 初始位置
setServoAngle(pin,0)
setServoAngle(pinUp,0)
time.sleep(2)
start = 90
startUp = 90
setServoAngle(pin,start)
setServoAngle(pinUp,startUp)


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
		change(image,[x,y],start,startUp)
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
        # GPIO.cleanup()
		break    


