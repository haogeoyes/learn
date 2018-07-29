#coding=UTF-8
import numpy as np
import cv2

img_path = '/Users/chenhaohao/git/learn/web/assets/image-20180623211349259.png'
img = cv2.imread(img_path,cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(150,150),(255,255,255),15)
cv2.rectangle(img,(15,25),(200,150),(0,255,0),5)
cv2.circle(img,(100,63),55,(0,0,255),-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255),5)

#文字
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
#cv2.putText(img,'OpenCV',(50,130),font,1,(200,255,255),2,cv2.LINE_AA)
cv2.putText(img,'OpenCV',(50,130),font,5,(200,255,255),5,cv2.LINE_AA)

#print(dir(cv2))
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()







'''
img[55,55] = [255,255,255]
px = img[55,55]
img[100:150,100:150] = [255,255,255]
watch_face = img[]
'''
