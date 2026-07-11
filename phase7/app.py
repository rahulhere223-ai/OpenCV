import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalcatface.xml")

cap=cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.1,5)

    # 
    # detectmultiscale()-scan and detect face
    # 1.1-balance ,not too slow,blind
    # 

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow("Webcam face detected",frame)

    if cv2.waitKey(1) & 0xFF== ord('q'):
        print("quitting....")
        break

cap.release()
cv2.destroyAllWindows()    