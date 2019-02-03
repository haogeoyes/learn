#coding=utf-8
'''
    树莓派上移动人体检测
	添加日志模块
    矩形框检测
'''
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

import numpy as np
import cv2
import logging




from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='log_background.log', level=logging.DEBUG, format=LOG_FORMAT)


width = 320
height = 240
camera = PiCamera()
camera.resolution = (width, height)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))
time.sleep(0.1)

 
def setServoAngle(servo, angle):
    # GPIO.setup(servo, GPIO.OUT)
    pwm = GPIO.PWM(servo, 50)
    pwm.start(8)
    dutyCycle = angle / 18. + 3.
    pwm.ChangeDutyCycle(dutyCycle)
    sleep(2)
    pwm.stop()
 
    # GPIO.cleanup()

def drawCenter(img,cnt,start,startUp):
    areaMin = 3000
    areaMax = 60000

    # 绘制重心
    cnts = []
    areaMaxNum = 0
    # max_x,max_y = [0,0]
    max_xy = [0,0]
    xy = [width/2,height/2]
    area = 0
    for i in cnt:
       # 面积
        area = cv2.contourArea(i)
        # if area > 5000 and  area < 60000:
        if area > areaMin and  area < areaMax:
            if area > areaMaxNum:
                areaMaxNum = area
                cntMax = i
                cnts.append(i)
                # print(i)
                print(area)
            # 重心坐标
            m = cv2.moments(i)
            if 'm01' in m and 'm10' in m and 'm00' in m:
                if m['m00'] !=0.0:
                    cx = int(m['m10']/m['m00'])
                    cy = int(m['m01']/m['m00'])
                    # max_x = cx
                    # max_y = cy
                    # print(cx,cy) 
                    xy = [cx,cy]
                    max_xy = xy

                    (x, y, w, h) = cv2.boundingRect(i)
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.circle(img,(cx,cy),3,(0,255,0),5)


    if areaMaxNum > areaMin and  areaMaxNum < areaMax:
        # change(img,xy,start)
        change(img,max_xy,start,startUp)
    # cnts.append(cntMax)
    # time.sleep(0.1)
    return [cnts,xy]
 



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
    print('弧度',start)
    # if radian > 0:
    if radian > 10:
        setServoAngle(pin,start)
        setServoAngle(pinUp,startUp)
    


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

# 算法代码
fgbg = cv2.createBackgroundSubtractorMOG2()

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    time.sleep(0.5)
    image = frame.array
    image = cv2.flip(image,0)
    img = image




    
    # 算法代码
    fgmask = fgbg.apply(image)


    # num = fgmask.mean()
    # print(num)
    # if num > 1:
    #     print('检测到有人活动')
    # logging.info(111111)



    # 二值化处理
    ret, binary = cv2.threshold(fgmask,127,255,cv2.THRESH_BINARY)  
    #轮廓查找
    img2,contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
    # 绘制重心
    [cnts,xy] = drawCenter(img,contours,start,startUp)

    # change(img,xy)

    # cv2.imshow('mask',fgmask)
    cv2.imshow('image',img)




    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    if key == ord("q"):
        GPIO.cleanup()
        break    


