#coding=utf-8
'''
    蓝色物体跟踪
'''
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        # 转换为hsv
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        # 设置蓝色阀值
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])
        #掩模
        mask = cv2.inRange(hsv,lower_blue,upper_blue)

        # add
        ret, binary = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)  
        img2,contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
        img = cv2.drawContours(frame,contours,3,(0,255,0),3)
        #运算
        res = cv2.bitwise_and(frame,frame,mask=mask)
        # cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('img',img)
        # cv2.imshow('res',res)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
