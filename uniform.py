#add uniform noise to image and plot the orignal and noisy image
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("Images/act.png",0)
cv2.imshow("orignal", img)
cv2.waitKey(0)
h,w = img.shape

noise = np.zeros((h,w), dtype=np.uint8)
cv2.randu(noise, 0, 255)
cv2.imshow("unifrom_noise", noise)
cv2.waitKey(0)

noisy_img = cv2.add(img, noise)
cv2.imshow("image_noise", noisy_img)
cv2.imwrite("Images/unifrom_noise.png", noisy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.plot(img[1], label="orignal", color='blue')
plt.plot(noise[1], label="noise", color='red')
plt.plot(noisy_img[1], label="noisy_img", color='green')
plt.legend()
plt.show()
