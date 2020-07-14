import cv2

#This is my webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    
    #here is a simple reading
    ret, back = cap.read()
    #ret is true if your camera is working and capturing
    #back is what the camera is reading ie the image
    if ret:
        cv2.imshow("image", back)
        #waitkye() - will wait for m milliseconds and then it will click a picture
        if cv2.waitKey(5) == ord('q'):
            # save image
            cv2.imwrite('image.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()