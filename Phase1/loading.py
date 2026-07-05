import cv2

image=cv2.imread("python_image.jpeg")

if image is None:
    print("Error image is not loaded successfully")
else:
    print("Image is loaded sucessfully")
