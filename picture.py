"""
作者：Mibbp
日期: 2022年01月04日
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def cv_show (name,img):
    cv.imshow(name,img)     #显示图像
    cv.waitKey(0)           # 等待时间，毫秒级，0表示任意键终止
    cv.destroyAllWindows()

img = cv.imread('01.jpg')   #读取照片
# cv_show('01',img)
# print(img.shape)    #图像三个参数，前两个参数是宽度和高度，第三个是颜色通道数量
#
# img1=img[0:50,0:200]    #截取照片
# cv_show('02',img1)
#
# b,g,r=cv.split(img)     #颜色通道提取，opencv是B-G-R
# print(b.shape)
#
# img=cv.merge((b,g,r))     #合并通道
#
# # 提取R通道 [:,:]长宽不设参数的话表示整张图片
# img2 = img.copy()
# img2[:,:,0]=0
# img2[:,:,1]=0
# cv_show('R',img2)

# 边界填充
top_size,bottom_size,left_size,right_size=(50,50,50,50)     #上下左右边界的值

# 复制法 复制最边缘元素
replicate =cv.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv.BORDER_REPLICATE)
cv_show('rep',replicate)

# 反射法 中间为原图像，左右为填充 fedcba|abcdefgh|hgfedcb
reflect =cv.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv.BORDER_REFLECT)
cv_show('ref',reflect)

# 反射法 以最边缘为轴，中间为原图像，左右为填充 fedcb|abcdefgh|gfedcb
reflect101 =cv.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv.BORDER_REFLECT_101)
cv_show('ref101',reflect101)

# 外包装法 gfedcb|abcdefgh|gfedcb
wrap =cv.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv.BORDER_WRAP)
cv_show('wrap',wrap)

# 常数法 直接填充指定的
con =cv.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv.BORDER_CONSTANT,10)
cv_show('con',con)