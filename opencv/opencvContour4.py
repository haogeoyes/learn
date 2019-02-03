#coding=utf-8
'''
    绘制轮廓4
    凸包
    识别图中的手，绘制矩形
'''
import numpy as np
import cv2

def initMain():
    # img = cv2.imread('react2.jpg')
    # img = cv2.imread('react2.jpeg')
    # img = cv2.imread('hand.jpeg')
    img = cv2.imread('hand2.jpeg')
    #灰度处理
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
    # 二值化处理
    ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
    #轮廓查找
    img2,contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
    # img2,contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)  
    # img2,contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_TC89_KCOS)  


    cnt = contours[1]
    # hull = cv2.convexHull(cnt)
    # hull = cv2.isContourConvex(cnt)

    # 边界矩形
    # x,y,w,h = cv2.boundingRect(cnt)
    # img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    drawCenter(img,contours)

    # 轮廓绘制
    # cv2.drawContours(img,contours,-1,(255,0,0),3)  

    # 绘制
    # out = drawCenter(img,contours)
    
    cv2.imshow("img", img)  
    cv2.waitKey(0) 
def drawCenter(img,cnt):
    # 绘制重心
    for i in cnt:
        # epsilon = 0.1*cv2.arcLength(i,True)
        # approx = cv2.approxPolyDP(i,epsilon,True)
        # cv2.circle(img,(cx,cy),3,(0,0,255),5)
        x,y,w,h = cv2.boundingRect(i)
        if w*h > 10000:
            print(w*h)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)




if '__main__' == __name__:
    initMain()




