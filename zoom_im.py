import numpy as np
import scipy as sp
import cv2
import random
from matplotlib import pyplot as plt

def zoom(img, factor):
    h,w,s = img.shape
    print (img.shape)
    z_h = factor*h
    z_w = factor*w
    cnt_h = 0
    cnt_w = 0
    x = 0
    y = 0
    z_img = np.empty((factor*h+1, factor*w+1, s), np.uint8)
    for i in range(z_h):
        y = 0
        for j in range(z_w):
            #print(i,j)
            #print(x,y)
            z_img[i][j] = img[x][y]
            cnt_w  = cnt_w + 1
            if (cnt_w % factor == 0):
                y = y+1
        cnt_h  = cnt_h + 1
        if (cnt_h % factor == 0):
            x = x+1
    return z_img


img = cv2.imread("images/flower.png")
d_img = zoom(img, 4)
cv2.imshow("orig", img)
cv2.waitKey(0)
cv2.imshow("d_img", d_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
