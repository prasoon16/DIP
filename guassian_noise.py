import numpy as np
import scipy as sp
import cv2
from matplotlib import pyplot as plt

def add_guass_noise(img, mu, sigma):
    rand = np.random.normal(mu, sigma, img.shape).astype(np.uint8)
    #plt.plot(rand.reshape())
    # cv2.imshow("rand", rand)
    # cv2.waitKey(0)
    print (rand[1,:10])
    return cv2.add(img, rand)

def plot_pixels(orignal, noisy, fil, bil):
    plt.plot(orignal, label="normal", color='r')
    plt.plot(noisy, label="noisy", color='b')
    plt.plot(fil, label="fil", color='g')
    plt.plot(bil, label="bil", color='y')
    plt.legend()
    plt.show()

img = cv2.imread("images/parrot.jpeg", 0)
img = cv2.resize(img, (200,200))
guass_img = add_guass_noise(img, 0, 1)
fil_img = cv2.GaussianBlur(guass_img, (9,9), 0)
bil_img = cv2.bilateralFilter(guass_img, 9, 75, 75)
cv2.imshow("orignal", img)
cv2.waitKey(0)
cv2.imshow("noisy_image", guass_img)
cv2.waitKey(0)
cv2.imshow("fil_img", fil_img)
cv2.waitKey(0)
cv2.imshow("bil_img", bil_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
plot_pixels(img[1], guass_img[100], fil_img[100], bil_img[100])
