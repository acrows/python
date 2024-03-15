# for each member, after creating the function python file,
# please use this python file to evaluate your funtion file.

from rgb_to_gray import *  # please import your python function file
import cv2

src = cv2.imread('img.jpg')
dst = rgb2gray(src)  # change this to your function
cv2.imwrite('eval_result.png', dst)
