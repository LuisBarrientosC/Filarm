#!/usr/bin/env python3
#encoding: utf-8

#ros library
import rospy

#camara library
from cv_bridge import CvBridge, CvBridgeError
import cv2
import imutils

#math and time
import time
import math
import numpy as np

#messages and services
from sensor_msgs.msg import Image
from sensor_msgs.msg import Joy
from std_msgs.msg import String,Float32

#global variables



class camara():

    def __init__(self):

        self.img_counter = 0
        self.vi_counter = 0
        self.vid=0

        self.bridge = CvBridge()

        self.frameWidth=640
        self.frameHeight=480

        self.cap  = cv2.VideoCapture(0)
        self.cap.set(3,self.frameWidth)
        self.cap.set(4,self.frameHeight)

        self.x_medium = int(640 / 2)
        self.y_medium = int(480 / 2)
        self.center = int(480 / 2)
        self.position = 90
        self.linea=0

        def empty(a):
            pass
        def dempty(b):
            pass

        self.img = self.cap.read()
        self.ret,self.frame= self.cap.read()
       #crate camara values
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

#get camara values
        self.hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        self.h_mi = cv2.getTrackbarPos("HUE Min", "HSV")
        self.h_ma = cv2.getTrackbarPos("HUE Max", "HSV")
        self.s_mi = cv2.getTrackbarPos("SAT Min", "HSV")
        self.s_ma = cv2.getTrackbarPos("SAT Max", "HSV")
        self.v_mi = cv2.getTrackbarPos("VALUE Min", "HSV")
        self.v_ma = cv2.getTrackbarPos("VALUE Max", "HSV")
        self.kmi = cv2.getTrackbarPos("ker Min", "kernel")
        self.kma = cv2.getTrackbarPos("ker Max", "kernel")
        self.it = cv2.getTrackbarPos("ite", "kernel")
        self.itd = cv2.getTrackbarPos("ited", "kernel")
        self.okmi = cv2.getTrackbarPos("oker Min", "kernel")
        self.okma = cv2.getTrackbarPos("Area Minima de deteccion", "kernel")
        self.lower_blue = np.array([self.h_mi, self.s_mi, self.v_mi])
        self.upper_blue = np.array([self.h_ma, self.s_ma, self.v_ma])
        self.kernel = np.ones((self.kmi, self.kma), np.uint8)
        self.okernel = np.ones((self.okmi, self.okma), np.uint8)
        self.erosion = cv2.erode(self.hsv, self.kernel, iterations=self.it)
        self.dilation = cv2.dilate(self.erosion, self.kernel, iterations=self.itd)
        
        self.opening = cv2.morphologyEx(self.dilation, cv2.MORPH_OPEN, self.okernel)
        self.closing = cv2.morphologyEx(self.opening, cv2.MORPH_CLOSE, self.kernel)

        self.mask = cv2.inRange(self.closing, self.lower_blue, self.upper_blue)
        self.result = cv2.bitwise_and(self.img, self.img, mask=self.mask)
        # imgray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        self.ret, self.thresh1 = cv2.threshold(self.mask, 127, 255, 0)
        self.contours, self.hierarchy = cv2.findContours(self.thresh1, 1, 2)
        cv2.drawContours(self.result, self.contours, -1, (0, 255, 0), 3)
        
        # cv2.imshow("mask", mask)
        self.linea_x=cv2.line(self.img, (320,0), (320,640), (0, 0, 0), 2)
        self.linea_y=cv2.line(self.img, (0,240), (640,240), (0, 0, 0), 2)
        cv2.imshow("Original",self.linea)
        # cv2.imshow("hsv", hsv)


        if len(self.contours) > 0:
            # Processing here.

            self.cnt = self.contours[0]
            # print(self.cnt)
            # M = cv2.moments(self.cnt)
            # print(M)
            # cx = int(M['m10'] / M['m00'])
            # cy = int(M['m01'] / M['m00'])
            self.area = cv2.contourArea(self.cnt)
            #print("area is: " + str(area))
            perimeter = cv2.arcLength(self.cnt, True)
            #print("perimeter is: " + str(perimeter))

            self.epsilon = 0.1 * cv2.arcLength(self.cnt, True)
            # print("elipson is: "+ str(self.epsilon))
            self.approx = cv2.approxPolyDP(self.cnt, self.epsilon, True)
            # print("approx is: " +str(approx))
            self.area_approx = cv2.contourArea(self.approx)
            #print("area_approx is: " + str(area_approx))
            self.hull = cv2.convexHull(self.cnt)
            self.area_hull = cv2.contourArea(self.hull)
            #print("area_hull is: " + str(area_hull))
            self.k = cv2.isContourConvex(self.cnt)
            x, y, w, h = cv2.boundingRect(self.cnt)
            cv2.rectangle(self.img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        else:
            print
            "Sorry No contour Found."

        cv2.imshow("result", self.result)

    def photo(self):

        img_name = "imagen_{}.png".format(self.img_counter) 
        cv2.imwrite(img_name, self.frame)
        print("{} written!".format(self.img_name)) 
        
        self.img_counter += 1 
    
    def video(self):
        
        if self.vid==0:
            codecs = cv2.VideoWriter_fourcc(*'MP4V')
            self.salida = cv2.VideoWriter('video_{}.mp4'.format(self.vi_counter),codecs,20.0,(640,480))
            self.vi_counter+=1
            self.vid=1
        
    def record_and_stop(self):

        if self.vid == 1:
            self.salida.write(self.frame)

def Photo_and_video_commands(data):

#Obtencion de los datos de los botones del control xbox
    A = data.buttons[0] 
    B = data.buttons[1]
    X = data.buttons[2]
    Y = data.buttons[3]
    RB = data.buttons[5]
    LB = data.buttons[4]
    UD = data.axes[7]
    DI = data.axes[6]
    SQ = data.buttons[6]
    
    if SQ == 1:
        use_camara.photo()
    
    if A == 1:
        use_camara.video()
    
    if B == 1:
        use_camara.vid = 0

if __name__ == "__main__":

#node initialization
    rospy.init_node('image' , anonymous = False)

#rate of readings
    rate = rospy.Rate(10)

#subcriptions
    rospy.Subscriber("joy", Joy, Photo_and_video_commands)

#publications
    pub_webcam = rospy.Publisher('/webcam' , Image, queue_size = 10)
    pub_position_x = rospy.Publisher('position_state_x' , Float32, queue_size = 10)
    pub_position_y = rospy.Publisher('position_state_y' , Float32, queue_size = 10)

    while True:
        use_camara = camara()
        use_camara.record_and_stop()
    
