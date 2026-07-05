import cv2

image=cv2.imread("python_image.jpeg")

h,w,c=image.shape

print(f"Image dimension:\n Height: {h} \n width:{w} \n color channel:{c}")