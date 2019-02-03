#coding=utf-8
'''
    绘制轮廓1
    视频轮廓检测
    绘制边界
'''
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)

def drawCenter(img,cnt):
    # 绘制重心
    for i in cnt:
        m = cv2.moments(i)
        cx = int(m['m10']/m['m00'])
        cy = int(m['m01']/m['m00'])
        # 重心坐标
        print(cx,cy) 
        # 面积
        area = cv2.contourArea(i)
        print(area)
        cv2.circle(img,(cx,cy),3,(0,0,255),5)
 


while(True):
    ret,frame = cap.read()
    #灰度处理
    imgray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # 二值化处理
    ret2,thresh = cv2.threshold(imgray,127,255,0)
    image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #绘制边界
    img = cv2.drawContours(frame,contours,3,(0,255,0),3)

    # drawCenter(img,contours)


    # cv2.imshow('frame',frame)
    # cv2.imshow('imgray',imgray)
    cv2.imshow('thresh',thresh)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()




