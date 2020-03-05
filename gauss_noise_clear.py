#clear gaussian noisy_image
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("Images/gauss_noise.png",0)
cv2.imshow("orignal", img)
cv2.waitKey(0)
f_img = cv2.GaussianBlur(img, (9,9),20)
cv2.imshow("noise_free", f_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.plot(img[1], label="orignal", color='blue')
plt.plot(f_img[1], label="noise_free", color='red')
#plt.plot(noisy_img[1], label="noisy_img", color='green')
plt.legend()
plt.show()
