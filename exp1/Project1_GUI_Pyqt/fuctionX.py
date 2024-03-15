import cv2
import numpy as np

def blur(img):
    radius = 5
    gray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    psf = gray.copy()
    psf[:,:] = 0

    cx = psf.shape[0]/2
    cy = psf.shape[1]/2

    rs = np.square(radius)

    for i in range(psf.shape[0]):
        for j in range(psf.shape[1]):
    #       print(i-cx,j-cy)
            if (np.square(i-cx) + np.square(j-cy) < rs):
                psf[i,j] = 255 # - 5*radius * (np.square(j-cx) + np.square(i-cy)).astype(int)


    f = np.fft.fft2(gray)
    p = np.fft.fft2(psf)

    s = f*p

    fshift = np.fft.fftshift(s)

    restore = np.fft.ifft2(fshift)
    sshift = np.fft.fftshift(restore)
    
    max_sshift = np.max(np.abs(sshift))

    img1 = (255 * np.abs(sshift)/max_sshift)
    img1 = img1.astype(np.uint8)
     
    dst = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
    
    return dst
    