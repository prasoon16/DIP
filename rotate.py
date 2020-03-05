#Use opncv rotate fucntion which uses rotate codes

import cv2
import numpy as np

im = cv2.imread("Images/coyote.jpg")
cv2.imshow("orignal", im)
cv2.waitKey(0)
im_ro = cv2.rotate(im, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("im_ro", im_ro)
cv2.waitKey(0)
cv2.destroyAllWindows()
