#coding=utf-8
'''
    图像金字塔 error
'''
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)

while(True):
    ret,frame = cap.read()

    lower_reso = cv2.pyrDown(higher_reso)



    cv2.imshow('frame',fgmask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()




