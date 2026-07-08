import cv2
import numpy as np

image = cv2.imread("median_blurred_image.jpeg")

sharpen_kernel=np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

sharpened=cv2.filter2D(image,-1,sharpen_kernel)

cv2.imshow("original image",image)
cv2.imshow("sharpened image",sharpened)

cv2.imwrite("sharpened_image2.jpeg",sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
