#coding=utf-8
'''
    绘制轮廓4
    凸包
    识别图中的手，绘制矩形
'''
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)


def initMain():

  while(True):
    ret,img = cap.read()

    #灰度处理
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
    # 二值化处理
    ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
    #轮廓查找
    img2,contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  

    # 边界矩形
    drawCenter(img,contours)

    # 轮廓绘制
    cv2.drawContours(img,contours,-1,(255,0,0),3)  
   
    cv2.imshow("img", img)  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  cap.release()
  cv2.destroyAllWindows()


def drawCenter(img,cnt):
    # 绘制重心
    for i in cnt:
        # 绘制矩形
        x,y,w,h = cv2.boundingRect(i)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


        # 绘制椭圆
        # elipse = cv2.fitEllipse(i)
        # cv2.ellipse(img,ellipse,(0,255,0),2)

        # print(w*h)
        if w*h > 10000:
            print(w*h)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            # 极值点
            leftmost = tuple(i[i[:,:,0].argmin()][0])
            rightmost = tuple(i[i[:,:,0].argmax()][0])
            topmost = tuple(i[i[:,:,1].argmin()][0])
            bottommost = tuple(i[i[:,:,1].argmax()][0])
            cv2.circle(img,leftmost,5,(0,0,255),20)
            cv2.circle(img,rightmost,5,(0,0,255),20)
            cv2.circle(img,topmost,5,(0,0,255),20)
            cv2.circle(img,bottommost,5,(0,0,255),20)




        # 绘制圆
        # (x,y),radius = cv2.minEnclosingCircle(i)
        # center = (int(x),int(y))
        # radius = int(radius)
        # if w*h > 10000:
        #    print(w*h)
        #    cv2.circle(img,center,radius,(0,255,0),2)







if '__main__' == __name__:
    initMain()




