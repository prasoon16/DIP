import numpy as np
import scipy as sp
import cv2
import random
from matplotlib import pyplot as plt

img = cv2.imread("images/sp_n.png", 0)
med = cv2.medianBlur(img, 9)
guass = cv2.GaussianBlur(med, (9,9), 0)
highpass = cv2.addWeighted(med, 1, guass, -1, 0)
highboost_image = cv2.addWeighted(med, 1.4, highpass, 1, 0)
cv2.imshow("orignal", img)
cv2.waitKey(0)
cv2.imshow("med", med)
cv2.waitKey(0)
cv2.imshow("highboost_image", highboost_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
