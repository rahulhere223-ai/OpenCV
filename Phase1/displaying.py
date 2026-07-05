import cv2

image=cv2.imread("python_image.jpeg")

if image is not None:
    cv2.imshow("Image showing",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image is loaded sucessfully")