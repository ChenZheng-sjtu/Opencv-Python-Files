# 检测圆


import cv2
import cv2.cv as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('eye.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # 图像转化为灰度图像

plt.subplot(121),plt.imshow(gray,'gray') #1代表行，2代表列，所以一共有2个图，1代表此时绘制第1个图
plt.xticks([]),plt.yticks([]) # 参数为空，代表不显示刻度


# 霍夫变换
circle1 = cv2.HoughCircles(gray,cv2.cv.CV_HOUGH_GRADIENT,1,100,param1=100,param2=30,minRadius=200,maxRadius=300)  
                            #把半径范围缩小点，检测内圆，瞳孔
if circle1 is None:
    exit(-1)
circles = circle1[0, :, :]  # 提取为二维
circles = np.uint16(np.around(circles))  # 四舍五入，取整


for i in circles[:]:
    cv2.circle(img,i[0],i[1],i[2],(255,0,0),5) # 画圆
    cv2.circle(img,i[0],i[1],2,(255,0,255),10) # 画圆心

plt.subplot(122),plt.show(img)
plt.xticks([]),plt.yticks([])

