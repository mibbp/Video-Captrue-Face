"""
作者：Mibbp
日期: 2022年01月06日
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def cv_show (name,img):
    cv.imshow(name,img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def face_detect_demo(img):
    gary=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier('D:/Users/mibbp/PycharmProjects/pythonProject1/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    face =face_detect.detectMultiScale(gary)
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
    # cv.namedWindow('a',0)
    # cv.resizeWindow('res',1200,600)
    cv.moveWindow('res',0,0)
    cv.imshow('res',img)


vc =cv.VideoCapture('beauty.mp4')   #读取视频
# 判断是否读取视频
if vc.isOpened():
    open,frame = vc.read()  #读取一帧画面
else :
    open=False

# 把视频每一帧读取出来
while open:
    ret, frame =vc.read()
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)    #将这一帧转换为灰色
    # cv.imshow('result',frame)                        #显示这一帧
    face_detect_demo(frame)
    if cv.waitKey(33) & 0xFF ==27:                  #等待时间，如果按倒关闭键则退出
        open=False
        break


# 释放并且销毁所有窗口
vc.release()
cv.destroyAllWindows()