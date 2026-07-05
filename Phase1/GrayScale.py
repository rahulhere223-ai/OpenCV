import cv2

image=cv2.imread("python_image.jpeg")

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayImage loaded",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

image1=cv2.imwrite("Gray_Image.jpeg",gray)
if image1:
    print("gray image saved")
else:
    print("image is not saved")    