#coding=utf-8
'''
    读取图像
    直方图
    摄像头
    绘制2d直方图 二维：颜色Hue 饱和度Saturation
'''
import numpy as np
import cv2
from matplotlib import pyplot as plt
cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)


while(True):
    ret,img = cap.read()
    # img = cv2.imread('background.png',0)
    # 从BGR转HSV
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    #算法
    hist = cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])

    # 显示
    # plt.subplot(221),plt.plot(hist)
    # plt.subplot(222),plt.imshow(hist,'gray')
    # plt.show()

    
    cv2.imshow("hist", hist)  
    cv2.imshow("img", img)  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()






