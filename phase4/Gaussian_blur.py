import cv2

image =cv2.imread("python_image.jpeg")

blurred=cv2.GaussianBlur(image,(9,9),4)

cv2.imwrite("blurred_image.jpeg",blurred)

cv2.imshow("Original image",image)
cv2.imshow("Blurred image",blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()