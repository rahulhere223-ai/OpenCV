import cv2


image=cv2.imread("Python_image.jpeg")

if image is  None:
    print("Image is not loaded")
else:
    print("Wait Image is loading.......")
    flipped_vertical=cv2.flip(image,0)
    flipped_horizontal=cv2.flip(image,1)
    flipped_both=cv2.flip(image,-1)

    cv2.imshow("Original Image",image)
    cv2.imshow("flipped_vertical Image",flipped_vertical)
    cv2.imshow("Flipped_Horizontal Image",flipped_horizontal)
    cv2.imshow("Flipped_both Image",flipped_both)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
