#coding=utf-8
'''
    绘制轮廓2
    轮廓的重心
'''
import numpy as np
import cv2

def initMain():
    img = cv2.imread('react.jpeg')
    #灰度处理
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
    # 二值化处理
    ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
    #轮廓查找
    img2,contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
    cv2.drawContours(img,contours,-1,(255,0,0),3)  

    # 绘制重心
    drawCenter(img,contours)
    
    cv2.imshow("img", img)  
    cv2.waitKey(0) 

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
        # 周长
        lenNum = cv2.arcLength(i,True)
        print(lenNum)
        cv2.circle(img,(cx,cy),3,(0,0,255),5)
 


if '__main__' == __name__:
    initMain()




