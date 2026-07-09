import cv2

img=cv2.imread("man.jpg",cv2.IMREAD_GRAYSCALE)

edges=cv2.Canny(img,80,150)

cv2.imshow("Orginal image",img)
cv2.imshow("Edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()