import cv2
import numpy as np

#jpg - 3 layers - depths rgb
#png - 4 layers/depths - rgba a- opacity

cap = cv2.VideoCapture(0)
back = cv2.imread('./image.jpg')

while cap.isOpened():
    #take each frame
    ret, frame = cap.read()
    # print(back.shape);
    if ret:
        # human eye sees the color in hsv format
        # because we se light, intensity and depths to these colours
        #how to convert rgb to hsv?
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # cv2.imshow("hsv", hsv)

        #how to get hsv value ?
        # lower: hue - 10, 100, 100, higher: hue+10, 255, 255
        teal = np.uint8([[[128,128,0]]]) #bgr value of red
        hsv_teal = cv2.cvtColor(teal, cv2.COLOR_BGR2HSV)
        #get hsv value of red from bgr
        # print(hsv_teal)

        #threshold the hsv value to get only red colors
        lower_teal = np.array([80,100,100]) #hue-10
        upper_teal = np.array([100,255,255]) #hue+10 

        #make the red color that fall in lower_red and upper_red range disappear
        mask = cv2.inRange(hsv, lower_teal, upper_teal)
        # cv2.imshow("mask", mask) #show only red color(white) and make other colors disappear

        #shows everything that is in the backgroud image when you see red color
        part1 = cv2.bitwise_and(back, back, mask=mask)
        # cv2.imshow("part1", part1)

        mask = cv2.bitwise_not(mask)

        #now display everthing that is not red
        part2 = cv2.bitwise_and(frame, frame, mask=mask)
        # cv2.imshow("mask", part2)

        #morphing
        kernel = np.ones((1,1),np.uint8)
        opening = cv2.morphologyEx(part1 + part2, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

        cv2.imshow("cloak", closing)

        if cv2.waitKey(5) == ord('q'):
            break
    
cap.release()
cv2.destroyAllWindows()