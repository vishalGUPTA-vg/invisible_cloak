import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
back = cv2.imread('./image.jpg')

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # cv2.imshow("hsv",hsv)
        #for red
        red = np.uint8([[[0, 0, 255]]])

        #for black
        # red = np.uint8([[[0, 0, 0]]])

        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
        # print(hsv_red)
        #for red

        l_red = np.array([0, 100, 100])
        u_red = np.array([10, 255, 255])
        mask = cv2.inRange(hsv, l_red, u_red)

        #for black

        # l_black = np.array([0, 0, 0])
        # u_black = np.array([50, 50, 100])
        #
        # mask = cv2.inRange(hsv, l_black, u_black)

        part1 = cv2.bitwise_and(back, back, mask=mask)
        mask = cv2.bitwise_not(mask)
        part2 = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow("cloak", part2 + part1)

        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
