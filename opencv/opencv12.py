#coding=utf-8
'''
    读取摄像头
    直方图
    x灰度值（0，255）
    y灰度值点数量
    多通道图绘制
'''
import numpy as np
import cv2
from matplotlib import pyplot as plt
cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)

while(True):
    ret,img = cap.read()
    color = ('b','g','r')
    # 处理为索引列获取
    for i,col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.show()
cap.release()
cv2.destroyAllWindows()




