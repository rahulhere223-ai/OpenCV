import cv2

image=cv2.imread("python_image.jpeg")

if image is None:
    print("OOps! Your image is not working")
else:
    print("Image is loaded Successfully")

    pt1=(50,100)
    pt2=(300,100)
    color=(255,0,0)
    thickness=4

    cv2.line(image,pt1,pt2,color,thickness)
    
    cv2.imshow("Line in Image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
