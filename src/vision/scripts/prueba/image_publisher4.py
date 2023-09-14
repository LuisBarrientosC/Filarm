#!/usr/bin/env python3

import imutils
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np
import time
from time import sleep
import math

frameWidth=640
frameHeight=480
cap = cv2.VideoCapture(2)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
global x_medium 
global y_medium
center = int(480 / 2)
position = 90
linea=0
ret,img = cap.read()
bridge = CvBridge()


def empty(a):
    pass
def dempty(b):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("HUE Min","HSV",0,179,empty)
cv2.createTrackbar("HUE Max","HSV",179,179,empty)
cv2.createTrackbar("SAT Min","HSV",0,255,empty)
cv2.createTrackbar("SAT Max","HSV",255,255,empty)
cv2.createTrackbar("VALUE Min","HSV",0,255,empty)
cv2.createTrackbar("VALUE Max","HSV",255,255,empty)

cv2.namedWindow("kernel")
cv2.resizeWindow("kernel",640,440)
cv2.createTrackbar("ker Min","kernel",0,10,dempty)
cv2.createTrackbar("ker Max","kernel",0,10,dempty)
cv2.createTrackbar("ite","kernel",0,10,dempty)
cv2.createTrackbar("ited","kernel",0,10,dempty)
cv2.createTrackbar("oker Min","kernel",0,10,dempty)
cv2.createTrackbar("Area Minima de deteccion","kernel",0,5000,dempty)

def ident():
            global x_medium
            global y_medium
            ret,img = cap.read()
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            h_mi = cv2.getTrackbarPos("HUE Min", "HSV")
            h_ma = cv2.getTrackbarPos("HUE Max", "HSV")
            s_mi = cv2.getTrackbarPos("SAT Min", "HSV")
            s_ma = cv2.getTrackbarPos("SAT Max", "HSV")
            v_mi = cv2.getTrackbarPos("VALUE Min", "HSV")
            v_ma = cv2.getTrackbarPos("VALUE Max", "HSV")
            kmi = cv2.getTrackbarPos("ker Min", "kernel")
            kma = cv2.getTrackbarPos("ker Max", "kernel")
            it = cv2.getTrackbarPos("ite", "kernel")
            itd = cv2.getTrackbarPos("ited", "kernel")
            okmi = cv2.getTrackbarPos("oker Min", "kernel")
            okma = cv2.getTrackbarPos("Area Minima de deteccion", "kernel")
            lower_blue = np.array([h_mi, s_mi, v_mi])
            upper_blue = np.array([h_ma, s_ma, v_ma])
            kernel = np.ones((kmi, kma), np.uint8)
            okernel = np.ones((okmi, okma), np.uint8)
            erosion = cv2.erode(hsv, kernel, iterations=it)
            dilation = cv2.dilate(erosion, kernel, iterations=itd)
         
            """
            # redish
            lower_blue = np.array([166, 63, 120])
            upper_blue = np.array([178, 255, 255])
            kernel = np.ones((3, 3), np.uint8)
            okernel = np.ones((0, 0), np.uint8)
            erosion = cv2.erode(hsv, kernel, iterations=2)
            dilation = cv2.dilate(erosion, kernel, iterations=2)
            """
            opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, okernel)
            closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

            mask = cv2.inRange(closing, lower_blue, upper_blue)
            result = cv2.bitwise_and(img, img, mask=mask)
           
            ret, thresh1 = cv2.threshold(mask, 127, 255, 0)
            contours, hierarchy = cv2.findContours(thresh1, 1, 2)
            cv2.drawContours(result, contours, -1, (0, 255, 0), 3)
            
            # cv2.imshow("mask", mask)
            linea_x=cv2.line(img, (320,0), (320,640), (0, 0, 0), 2)
            linea_y=cv2.line(img, (0,240), (640,240), (0, 0, 0), 2)
            cv2.imshow("Original",linea)
            # cv2.imshow("hsv", hsv)


            if len(contours) > 0:
                # Processing here.

                cnt = contours[0]
                
                area = cv2.contourArea(cnt)
                
                perimeter = cv2.arcLength(cnt, True)

                epsilon = 0.1 * cv2.arcLength(cnt, True)
               
                approx = cv2.approxPolyDP(cnt, epsilon, True)
                
                area_approx = cv2.contourArea(approx)
                
                hull = cv2.convexHull(cnt)
                area_hull = cv2.contourArea(hull)
                
                k = cv2.isContourConvex(cnt)
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            else:
                print
                "Sorry No contour Found."

            cv2.imshow("result", result)

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 3)
            thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
           
            cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
      
            
            # loop over the contours
            for c in cnts:
                if cv2.contourArea(c) > okma:
                    # compute the center of the contour
                    M = cv2.moments(c)
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    # draw the contour and center of the shape on the image
                    #cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
                    cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
                    cv2.putText(img, "center", (cX - 20, cY - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                    x_medium = int((x + x + w) / 2)
                    y_medium = int((y + y + h) / 2)
                    cv2.line(img, (x_medium, 0), (x_medium, 480), (0, 0, 255), 2)
                    cv2.line(img, (0,y_medium), ( 640, y_medium), (0, 0, 255), 2)


                    
                break
            
            print(center)
            print("X_position is: ",x_medium)
            print("Y_position is: ",y_medium)

            cv2.imshow("Original",img)

            return img


def talker():
    pub = rospy.Publisher('/webcam' , Image, queue_size = 100)
    rospy.init_node('image' , anonymous = False)
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        ident()
        ret, frame = cap.read()
        if not ret:
            break

        msg = bridge.cv2_to_imgmsg( frame, "bgr8")
        pub.publish(msg)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()

if __name__ == '__main__':
    try:
            talker()

    except rospy.ROSInterruptException:
        pass
