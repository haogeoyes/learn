#coding=utf-8
'''
    人体识别
'''
import numpy as np
import cv2
import time

from imutils.video import VideoStream
from imutils.video import FPS
import imutils




cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)

# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

while(True):
    ret,frame = cap.read()
    img = frame

    # 绘制重心
    # cnts = drawCenter(img,contours)
    # cv2.drawContours(frame,cnts,-1,(255,0,0),3)  



    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()




# ------------视频双击未完成------
# def draw_circle(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         print(x,y)
#         cv2.circle(img,(x,y),100,(255,0,0),-1)




# while(cap.isOpened()):
#     ret,img = cap.read()
#     cv2.namedWindow('image')
#     cv2.setMouseCallback('image',draw_circle)
#     if ret == True:
#         cv2.imshow('image',img)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
# cap.release()
# out.release()
# cv2.destroyAllWindows()
