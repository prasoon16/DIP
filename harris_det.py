import cv2
import numpy as np

def harris(im):
    img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    img = np.float32(img)
    dst = cv2.cornerHarris(img, 2 ,3, 0.04)
    dst = cv2.dilate(dst,None)
    im[dst>0.01*dst.max()]=[0,0,255]
    return im


im1= cv2.imread("Images/h.png")
im2 = cv2.imread("Images/h1.png")
cv2.imshow("im1", im1)
cv2.waitKey(0)
cv2.imshow("im2", im2)
cv2.waitKey(0)

dest1 = harris(im1)
dest2 = harris(im2)

cv2.imshow("dest1", dest1)
cv2.waitKey(0)
cv2.imshow("dest2", dest2)
cv2.waitKey(0)
cv2.destroyAllWindows()
