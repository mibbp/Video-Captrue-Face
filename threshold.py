"""
作者：Mibbp
日期: 2022年01月04日
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

def cv_show(name,img):
    cv.imshow(name,img)
    cv.waitKey(0)
    cv.destroyAllWindows()

#   dst = cv.threshold(src,thresh,maxval,type)
#   src 输入图，单通道，通常为灰度图
#   thresh 阈值 常见为127
#   maxval  最大值通常为255
#   type 二值化操作类型，以下5种：
#   THRESH_BINARY 超过阈值去maxval,否则取0
#   THRESH_BINARY_INV 上面那个反过来
#
#
img = cv.imread('01.jpg')

