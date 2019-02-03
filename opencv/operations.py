#coding=UTF-8
import numpy as np
import cv2

img_path = 'timg.jpeg'
img = cv2.imread(img_path,cv2.IMREAD_COLOR)

'''
img = [[254 254 254]
  [254 254 254]
  [254 254 254]
  ...
  [239 239 239]
  [239 239 239]
  [239 239 239]]]
'''

#图像位置
px = img[55,55]

#修改图像颜色为白色像素
img[55,55] = [255,255,255]

#图像区域 ROI  Region of Image
#print(img)

roi = img[100:150,100:150]

img[100:150,100:150] = [255,255,255]

#复制
watch_face = img[37:111,107:194]
img[0:74,0:87] = watch_face


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

















