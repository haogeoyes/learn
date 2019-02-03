#coding=utf-8
'''
    读取图像
    直方图
    x灰度值（0，255）
    y灰度值点数量
    使用掩模
'''
import numpy as np
import cv2
from matplotlib import pyplot as plt
cap = cv2.VideoCapture(0)
# cap.set(3,320)
# cap.set(4,240)
ret,img = cap.read()

# 创建掩模
mask = np.zeros(img.shape[:2],np.uint8)
mask[100:300,100:400] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)

histr_full = cv2.calcHist([img],[0],None,[256],[0,256])
histr_mask = cv2.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(221),plt.imshow(img,'gray')
plt.subplot(222),plt.imshow(mask,'gray')
plt.subplot(223),plt.imshow(masked_img,'gray')
plt.subplot(224),plt.plot(histr_full),plt.plot(histr_mask)
plt.xlim([0,256])
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






