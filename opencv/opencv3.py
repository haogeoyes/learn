#coding=utf-8
'''
    显示视频
'''
import numpy as np
import cv2
cap = cv2.VideoCapture(0)

# 摄像头是否准备就绪
init = cap.isOpened()
print(init)

# 打开摄像头异常替代方案
# cap.open()

# 获取视频属性0-18
# option = cap.get(3)
# print(cap.get(3),cap.get(4))  #每一帧宽度和高度

# 修改视频属性
# 窗口宽度和高度
cap.set(3,320)
cap.set(4,240)


while(True):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()