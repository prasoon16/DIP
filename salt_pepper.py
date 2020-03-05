import cv2
import numpy as np
import random

def add_sp_noise(img, prob):
    thres = 1 - prob
    h,w = img.shape
    im = np.empty(img.shape, np.uint8)
    for i in range(h):
        for j in range(w):
            r = random.random()
            if (r<prob):
                im[i][j] = 0
            elif (r>thres):
                im[i][j] = 255
            else:
                im[i][j] = img[i][j]
    return im

img = cv2.imread("Images/act.png",0)
cv2.imshow("orignal", img)
noisy_im = add_sp_noise(img, 0.2)
cv2.imshow("noisy_im", noisy_im)
cv2.imwrite("images/noisy_im.png", noisy_im)
