import cv2


image=cv2.imread("Python_image.jpeg")

if image is  None:
    print("Image is not loaded")
else:
    print("Wait Image is loading.......")
    h,w,c=image.shape
    center=(w//2,h//2)
    M=cv2.getRotationMatrix2D(center,90,1.0)
    rotated_image=cv2.warpAffine(image,M,(w,h))

    cv2.imshow("Original image",image)
    cv2.imshow("Rotated image",rotated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
