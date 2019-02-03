#coding=utf-8
'''
    显示灰度图像 esc 退出  s保存
'''
import numpy as np
import cv2
img = cv2.imread('img_tem.png',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:
    # esc 退出
    cv2.destroyAllWindows() 
elif k == ord('s'):
    #s 保存退出
    cv2.imwrite('1.png',img) 
    cv2.destroyAllWindows()