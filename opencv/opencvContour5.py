#coding=utf-8
'''
    绘制轮廓5
    凸包
    点间距 最远距离
'''
import numpy as np
import cv2

def initMain():
    img = cv2.imread('react2.jpg')
    # img = cv2.imread('react2.jpeg')
    # img = cv2.imread('hand.jpeg')
    img = cv2.imread('hand2.jpeg')
    #灰度处理
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
    # 二值化处理
    ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
    #轮廓查找
    img2,contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
    # img2,contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)  
    # img2,contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_TC89_KCOS)  


    # hull = cv2.convexHull(cnt)
    # hull = cv2.isContourConvex(cnt)

    # 边界矩形
    # x,y,w,h = cv2.boundingRect(cnt)
    # img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    drawCenter(img,contours)

    # 轮廓绘制
    # cv2.drawContours(img,contours,-1,(255,0,0),3)  
   
    cv2.imshow("img", img)  
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
def drawCenter(img,cnt):


    for i in cnt:
        # 检测中心点距离轮廓距离
        point = (500,500)
        dist = cv2.pointPolygonTest(i,point,True)
        # print(dist)
        if dist > 0:
            print(dist)

        # 凸检测
        hull = cv2.convexHull(i,returnPoints = False)
        defects = cv2.convexityDefects(i,hull)
        # print(isinstance(defects,list))
        # if type(defects).__name__ == "ndarray":
        if type(defects).__name__ == "ndarray" and dist > 0:
            for j in range(defects.shape[0]):
                s,e,f,d = defects[j,0]
                start = tuple(i[s][0])
                end = tuple(i[e][0])
                far = tuple(i[f][0])
                # print(start,end,far)  #点坐标 开始 结束  最远坐标
                cv2.line(img,start,end,[0,255,0],2)
                cv2.circle(img,far,5,[0,0,255],-1)






if '__main__' == __name__:
    initMain()




