#coding=utf-8
'''
    读取图像
    直方图
    反向投影  找出特定区域 在图像中匹配的对象
    去矩形中的颜色，找出图片相同的颜色
'''
import numpy as np
import cv2
from matplotlib import pyplot as plt



cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)


while(True):
    ret,img = cap.read()
    x = 50
    y = 50
    w = 100
    h = 100
    # img = cv2.imread('background.png',0)
    # 从BGR转HSV

    # 原始部分
    hsvt = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # 取样部分
    hsv = hsvt[y:y+h, x:x+w]
	
    #算法
    # 直方图
    hist = cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
    cv2.normalize(hist,hist,0,255,cv2.NORM_MINMAX)
    #直方图反向投影
    dst = cv2.calcBackProject([hsvt],[0,1],hist,[0,180,0,256],1)
    # 卷积处理把分散的点连起来
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    dst = cv2.filter2D(dst,-1,disc)
    ret,thresh = cv2.threshold(dst,50,255,0)
    thresh = cv2.merge((thresh,thresh,thresh))
    # thresh = cv2.merge((thresh,thresh,thresh))
    res = cv2.bitwise_and(img,thresh)

    # 显示三通道图像
    # res = np.hstack((img,thresh,res))

    
    cv2.rectangle(res,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.rectangle(thresh,(x,y),(x+w,y+h),(255,0,0),2)
    # cv2.imshow("hist", hist)  
    cv2.imshow("img", img)  
    cv2.imshow("img", thresh)    
    cv2.imshow("img", res)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()






