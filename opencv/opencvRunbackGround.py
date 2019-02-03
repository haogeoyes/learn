#coding=utf-8
'''
    背景消除，移动物体检测
    轮廓检测
    颜色检测
'''
import numpy as np
import cv2
import time
cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)

# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))


def drawCenter(img,cnt):
    # 绘制重心
    cnts = []
    areaMax = 0
    for i in cnt:
       # 面积
        area = cv2.contourArea(i)
        if area > 2000 and  area < 60000:
            if area > areaMax:
                areaMax = area
                cntMax = i
                cnts.append(i)
                # print(i)
                print(area)
            # 重心坐标
            m = cv2.moments(i)
            if 'm01' in m and 'm10' in m and 'm00' in m:
                if m['m00'] !=0.0:
                    cx = int(m['m10']/m['m00'])
                    cy = int(m['m01']/m['m00'])
                    print(cx,cy) 

                    (x, y, w, h) = cv2.boundingRect(i)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.circle(frame,(cx,cy),3,(0,255,0),5)
    # cnts.append(cntMax)
    # 周长
    # lenNum = cv2.arcLength(i,True)
    # print(lenNum)
    # cv2.circle(img,(cx,cy),3,(0,0,255),5)
    # time.sleep(0.1)
    return cnts
 

fgbg = cv2.createBackgroundSubtractorMOG2()
while(True):
    ret,frame = cap.read()
    img = frame
    # 移动检测
    fgmask = fgbg.apply(frame)

    #灰度处理
    gray = fgmask
    # 二值化处理
    ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
    #轮廓查找
    img2,contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  

    # 绘制重心
    cnts = drawCenter(img,contours)
    # cv2.drawContours(frame,cnts,-1,(255,0,0),3)  



    cv2.imshow('frame',fgmask)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()




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
