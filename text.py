import numpy as np
import scipy as sp
import cv2
import random
from matplotlib import pyplot as plt

img = cv2.imread("images/text.png")
med = cv2.medianBlur(img, 3)
avg = cv2.blur(img, (5,5))
blur = cv2.GaussianBlur(img,(5,5),0)
dt2 = img - avg
dt1 = img - blur
boost = img + dt2
boost1 = img + dt1
cv2.imshow("orignal", img)
cv2.waitKey(0)
cv2.imshow("avg", avg)
cv2.waitKey(0)
cv2.imshow("dt2", dt2)
cv2.waitKey(0)
cv2.imshow("boost", boost)
cv2.waitKey(0)
cv2.imshow("dt1", dt1)
cv2.waitKey(0)
cv2.imshow("boost1", boost1)
cv2.waitKey(0)
cv2.destroyAllWindows()
