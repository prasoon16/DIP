import cv2

# Load the image
image = cv2.imread("images/face.png", 0)
# Blur the image
lowpass = cv2.GaussianBlur(image, (7,7), 0)
highpass = cv2.addWeighted(image, 1, lowpass, -1, 0)
# Apply Unsharp masking
highboost_image = cv2.addWeighted(image, 1.4, highpass, 1, 0)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.imshow("lowpass", lowpass)
cv2.waitKey(0)
cv2.imshow("highpass", highpass)
cv2.waitKey(0)
cv2.imshow("highboost_image", highboost_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
