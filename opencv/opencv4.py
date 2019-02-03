#coding=utf-8
'''
    保存视频
'''
import numpy as np
import cv2
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        # 垂直方向旋转180度
        # frame = cv2.flip(frame,0) 
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()

# 无法打开视频,确保安装了ffmpeg gstreamer ？？？？？？