import cv2

image = cv2.imread("python_image.jpeg")

if image is None:
    print("Image  is not loaded")
else:
    print("Image is loaded sucessfully")

    pt1=(50,50)
    pt2=(250,200)
    color=(255,0,0)
    thickness=-1

    cv2.rectangle(image,pt1,pt2,color,thickness)

    cv2.imshow("Rectangle drawn",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    