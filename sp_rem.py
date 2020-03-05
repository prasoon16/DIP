import cv2
import numpy as np

img = cv2.imread("Images/noisy_im.png",0)
cv2.imshow("orignal", img)
cv2.waitKey(0)
n_im = cv2.medianBlur(img, 3)
cv2.imshow("n_im", n_im)
cv2.waitKey(0)
