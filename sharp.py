import cv2

# Load the image
image = cv2.imread("images/text.png", 0)
# Blur the image
lowpass = cv2.GaussianBlur(image, (9,9), 10)
sharp = cv2.addWeighted(image, 1, lowpass, -1, 0)
h_boost = cv2.addWeighted(image, 1.4, sharp, 1, 0)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.imshow("lowpass", lowpass)
cv2.waitKey(0)
cv2.imshow("sharp", sharp)
cv2.waitKey(0)
cv2.imshow("h_boost", h_boost)
cv2.waitKey(0)
cv2.destroyAllWindows()
