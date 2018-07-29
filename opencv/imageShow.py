#coding=UTF-8
import cv2
import numpy as np 
import matplotlib.pyplot as plt
img_path = '/Users/chenhaohao/git/learn/web/assets/image-20180623211349259.png'
img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
