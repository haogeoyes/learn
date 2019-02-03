#coding=utf-8
'''
    直方图
    x灰度值（0，255）
    y灰度值点数量
'''
import numpy as np
import cv2
from matplotlib import pyplot as plt
cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)

while(True):
    ret,frame = cap.read()
    #灰度处理
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #原图像、图像灰度012对应BGR、掩模图像某一部分、BIN数量、像素范围
    hist = cv2.calcHist([gray],[0],None,[256],[0,256])


    # 彩色图像绘制直方图
    plt.hist(frame.ravel(),256,[0,256])
    # 灰度图像绘制
    # plt.hist(hist)
    plt.show()
    #绘制直方图
    # print(hist)

    # cv2.imshow('gray',gray)
    # cv2.imshow('hist',hist)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
cap.release()
cv2.destroyAllWindows()




