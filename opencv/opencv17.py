#coding=utf-8
'''
    读取图像
    直方图
    x灰度值（0，255）
    y灰度值点数量
    直方图的均值化 在人脸识别、训练分类器之前 是所有图像达到相同的亮度条件
    缺点在像素点变化很大，既有很亮的像素点又有很暗的像素点,像素值没有集中在某一区域
    CLAHE有限对比适应性直方图均值化
    对复杂背景识别
'''
import numpy as np
import cv2
from matplotlib import pyplot as plt
# cap = cv2.VideoCapture(0)
# cap.set(3,320)
# cap.set(4,240)
# ret,img = cap.read()
img = cv2.imread('background.png',0)


#算法
clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
res = clahe.apply(img)
# equ = cv2.equalizeHist(img)
# res = np.hstack((img,equ))

plt.subplot(221),plt.plot(res)
plt.subplot(222),plt.imshow(res,'gray')

# plt.plot(res) 
# plt.imshow(res,'gray')
plt.show()

# color = ('b','g','r')
# # 处理为索引列获取
# for i,col in enumerate(color):
#     histr = cv2.calcHist([img],[i],None,[256],[0,256])
#     plt.plot(histr,color = col)
#     plt.xlim([0,256])
# plt.show()
# cap.release()
# cv2.destroyAllWindows()






