"""
作者：Mibbp
日期: 2022年01月04日
"""
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def cv_show(name,img):
    cv.imshow(name,img)
    cv.waitKey(0)
    cv.destroyAllWindows()
# 图像融合 shape值必须一样
img1 = cv.imread('03.jpg')
img2 = cv.imread('01.jpg')

img2 = cv.resize(img2,(942,785))    #转换shape值
res = cv.addWeighted(img1, 0.4, img2, 0.6, 0)

cv_show('4',res)
