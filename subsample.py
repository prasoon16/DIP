import numpy as np
import scipy as sp
import cv2
import random
from matplotlib import pyplot as plt

def sub_sample(img, factor):
    h,w,sh = img.shape
    dest = np.empty((int(h/factor + 1),int(w/factor + 1),sh), np.uint8)
    cnt_r = 0
    cnt_c = 0
    x = 0
    y = 0
    print (h/2,w/2)
    for i in range(h):
        if (cnt_r % factor == 0):
            y = 0
            for j in range(w):
                if (cnt_c % factor == 0):
                    #print(x,y)
                    dest[x][y] = img[i][j]
                    y = y + 1
                cnt_c = cnt_c + 1
            x = x + 1
        cnt_r = cnt_r + 1
    return dest




img = cv2.imread("images/pic1.png")
h_image = sub_sample(img, 2)
t_image = sub_sample(img, 3)
f_image = sub_sample(img, 4)
print(img.shape, h_image.shape)
cv2.imshow("orignal", img)
cv2.waitKey(0)
cv2.imshow("half", h_image)
cv2.waitKey(0)
cv2.imshow("third", t_image)
cv2.waitKey(0)
cv2.imshow("fourth", f_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
