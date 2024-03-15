import cv2
#img=cv2.imread("Z:\A_cslg\python\task1\\1.png",1) #文件绝对路径
img=cv2.imread(".\\1.png",1) #文件相对路径下提前存放一个对应文件名的图片
cv2.imshow("test image",img) 
cv2.waitKey()   #实现方式
