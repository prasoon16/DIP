import numpy as np
import scipy as sp
import cv2
import random
from matplotlib import pyplot as plt

def plot_pixels(orignal, noisy, fil):
    plt.plot(orignal, label="normal", color='r')
    plt.plot(noisy, label="noisy", color='b')
    plt.plot(fil, label="fil", color='g')
    plt.legend()
    plt.show()

def add_sp_noise(img, prob):
    thres = 1 - prob
    h,w,s = img.shape
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



img = cv2.imread("images/parrot.jpeg")
img = cv2.resize(img, (200,200))
sp_img = add_sp_noise(img, 0.05)
med_img = cv2.medianBlur(sp_img, 5)
cv2.imshow("orignal", img)
cv2.waitKey(0)
cv2.imshow("sp_image", sp_img)
cv2.waitKey(0)
cv2.imshow("med_img", med_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
plot_pixels(img[20], sp_img[20], med_img[20])
