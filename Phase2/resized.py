import cv2

image=cv2.imread("python_image.jpeg")


if image is None:
    print("Image is not found")
else:
    print("Image is loaded")

    resized=cv2.resize(image,(300,300)) #width,Height 

    cv2.imshow("Original Image",image)
    cv2.imshow("Resize Image",resized)

    cv2.imwrite("Resized_output_image.jpeg",resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
