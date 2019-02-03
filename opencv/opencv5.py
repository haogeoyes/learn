#coding=utf-8
'''
    画画
'''
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        # 垂直方向旋转180度
        # frame = cv2.flip(frame,0) 
        # 画线
        cv2.line(frame,(0,100),(511,100),(255,0,0),5)
        # 矩形
        cv2.rectangle(frame,(50,150),(300,200),(255,0,0),5)
        # 圆
        cv2.circle(frame,(200,200),50,(255,0,0),5)
        out.write(frame)
        #文字
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,'test',(10,500),font,4,(255,255,255),2)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()

# 无法打开视频,确保安装了ffmpeg gstreamer ？？？？？？