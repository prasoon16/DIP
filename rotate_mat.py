import cv2
import numpy as np

im = cv2.imread("Images/coyote.jpg")
h,w = im.shape[:2]
cv2.imshow("orignal", im)
cv2.waitKey(0)
mat = cv2.getRotationMatrix2D((w/2,h/2), 40, 1)
cos = np.abs(mat[0,0])
sin = np.abs(mat[0,1])
nw = int(w*cos + h*sin)
nh = int(h*cos + w*sin)
mat[0,2] = mat[0,2] + (nw/2) - w//2
mat[1,2] = mat[1,2] + (nh/2) - h//2
rot_im = cv2.warpAffine(im, mat, (nw,nh))
cv2.imshow("rot_im", rot_im)
cv2.waitKey(0)
cv2.destroyAllWindows()
