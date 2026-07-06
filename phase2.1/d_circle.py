import cv2

image = cv2.imread("python_image.jpeg")

if image is None:
    print("Image  is not loaded")
else:
    print("Image is loaded sucessfully")

    pt1=(250,250)
    radius=50
    color=(255,0,0)
    thickness=-1

    cv2.circle(image,pt1,radius,color,thickness)

    cv2.imshow("Rectangle drawn",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    