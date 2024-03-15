import cv2

def function6(img):
    dst =  cv2.flip(img, 0) 
    dst =  cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
    return dst
    
