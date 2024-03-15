import cv2

def myproc(img):
    dst =  cv2.flip(img, 1) 
    dst =  cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
    return dst
    
