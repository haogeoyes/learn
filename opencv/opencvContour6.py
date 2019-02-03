#coding=utf-8
'''
    绘制轮廓6
    形状匹配
    返回轮廓组织结构、父子罗轮廓
    下一轮廓、上一轮廓、第一个子轮廓、第二个子轮廓
''' 
import numpy as np
import cv2

def initMain():
    img1 = cv2.imread('stars.png')
    img2 = cv2.imread('stars_one.png')  #要匹配的图像

    #灰度 二值化 处理
    gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)  
    ret, binary1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
    gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)  
    ret, binary2 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  

    # 图像、轮廓、层次结构
    img,contours1,hierarchy1 = cv2.findContours(binary1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
    img,contours2,hierarchy2 = cv2.findContours(binary2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  

    #下一轮廓、上一轮廓、第一个子轮廓、第二个子轮廓
    print(hierarchy1)
    print(hierarchy2)
    # ret = cv2.matchShapes(cnt1,cnt2,1,0,0)
    # print(ret)

    # 绘制匹配到图像
    # cv2.drawContours(img1,contours1,-1,(255,0,0),3)  
    # cv2.drawContours(img2,contours2,-1,(255,0,0),3)  

    #匹配形状
    drawCenter(contours1,contours2,img1,img2)


    cv2.imshow("img1", img1)  
    cv2.imshow("img2", img2)  
    cv2.waitKey(0) 
    cv2.destroyAllWindows()

def drawCenter(cnt1,cnt2,img1,img2):
    for i in cnt1:
        for j in cnt2:
            ret = cv2.matchShapes(i,j,1,0.0)
            print(ret)
            if ret < 0.2:
                cv2.drawContours(img1,i,-1,(255,0,0),3)  
                # cv2.drawContours(img2,j,-1,(255,0,0),3)  
            # area = cv2.contourArea(i)
            # print(area)


  
    # cv2.imshow("img", img)  
    # cv2.waitKey(0) 
    # cv2.destroyAllWindows()





if '__main__' == __name__:
    initMain()




