"""
作者：Mibbp
日期: 2022年01月04日
"""
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

vc =cv.VideoCapture('02.mp4')   #读取视频
# 判断是否读取视频
if vc.isOpened():
    open,frame = vc.read()  #读取一帧画面
else :
    open=False

# 把视频每一帧读取出来
while open:
    ret, frame =vc.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)    #将这一帧转换为灰色
    cv.imshow('result',gray)                        #显示这一帧

    if cv.waitKey(33) & 0xFF ==27:                  #等待时间，如果按倒关闭键则退出
        open=False
        break


# 释放并且销毁所有窗口
vc.release()
cv.destroyAllWindows()