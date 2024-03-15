import cv2

def rgb2gray(img):
    dst =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    return dst
    
