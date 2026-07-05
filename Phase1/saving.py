import cv2

image=cv2.imread("python_image.jpeg")

if image is not None:
    success=cv2.imwrite("Output_image.jpeg",image)
    if success:
        print("Image saved successfully")
    else:
        print("Image is not loaded")    
else:
    print("Error: There is some problem")