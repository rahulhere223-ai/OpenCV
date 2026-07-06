import cv2

image=cv2.imread("python_image.jpeg")

if image is not None:
    print("Image is loading successfully.....")
    cropped=image[100:200,50:150]

    cv2.imshow("Original Image",image)
    cv2.imshow("cropped image",cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image is not loaded")    