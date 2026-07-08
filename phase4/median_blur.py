import cv2

image=cv2.imread("python_image.jpeg")

blurred=cv2.medianBlur(image,9)

cv2.imshow("Original image",image)
cv2.imshow("Median_blurred image",blurred)
cv2.imwrite("median_blurred_image.jpeg",blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()

