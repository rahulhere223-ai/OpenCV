import cv2

image = cv2.imread("python_image.jpeg")

if image is None:
    print("Image  is not loaded")
else:
    print("Image is loaded sucessfully")

    cv2.putText(image,"Handsome Boy",(250,250),cv2.FONT_HERSHEY_SIMPLEX,1.2,(0,255,0),2)


    cv2.imshow("Put text in image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    