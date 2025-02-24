import numpy as np
import scipy as sp
import cv2
import random
from matplotlib import pyplot as plt

img = cv2.imread("images/noisy.png")
med = cv2.medianBlur(img, 3)
avg = cv2.blur(img, (3,3))
cv2.imshow("orignal", img)
cv2.waitKey(0)
cv2.imshow("med", med)
cv2.waitKey(0)
cv2.imshow("avg", avg)
cv2.waitKey(0)
cv2.destroyAllWindows()
