#coding=utf-8
'''
    边界检测1
    梯度计算
'''
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)

def nothing(x):
    pass


while(True):
    ret,frame = cap.read()
    fgmask = cv2.Canny(frame,100,200)

    # switch = '0:OFF\n1:ON'
    # cv2.createTrackbar(switch,'frame',0,1,nothing)
    cv2.imshow('frame',fgmask)
    cv2.createTrackbar('minVal','frame',0,1000,nothing)
    cv2.createTrackbar('maxVal','frame',0,1000,nothing)
    minVal = cv2.getTrackbarPos('minVal','frame')
    maxVal = cv2.getTrackbarPos('maxVal','frame')
    # s = cv2.getTrackbarPos(switch,'frame')
    # if s == 0:
    #     frame[:] = 0
    # else:
    #     frame[:] = [minVal,maxVal]
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()




