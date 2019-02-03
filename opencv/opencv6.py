#coding=utf-8
'''
    鼠标双击画圆
'''
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)

# 监听函数
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(True):
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




# ------------视频双击未完成------
# def draw_circle(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         print(x,y)
#         cv2.circle(img,(x,y),100,(255,0,0),-1)




# while(cap.isOpened()):
#     ret,img = cap.read()
#     cv2.namedWindow('image')
#     cv2.setMouseCallback('image',draw_circle)
#     if ret == True:
#         cv2.imshow('image',img)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
# cap.release()
# out.release()
# cv2.destroyAllWindows()
