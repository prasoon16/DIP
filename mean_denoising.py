import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("Images/unifrom_noise.png")
n_img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
cv2.imshow("orignal", img)
cv2.waitKey(0)
cv2.imshow("n_img", n_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
