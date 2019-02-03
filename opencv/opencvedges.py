#coding=utf-8
'''
    边缘检测
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
        # 边缘检测
        edges = cv2.Canny(frame,100,200)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',edges)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
