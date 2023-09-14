
#!/usr/bin/env python3
#encoding: utf-8
# -*- coding: utf-8 -*-
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import imutils
import numpy as np
import time
from time import sleep
import math
from std_msgs.msg import String,Float32
from sensor_msgs.msg import Joy

bridge = CvBridge()
img_counter = 0
vi_counter = 0
vid=0
x=0
z=0
u=1
i=1
j=0
A=0.0   
B=0.0
X=0.0
Y=0.0
RB=0.0
LB=0.0
LT=0.0
DI=0.0  #Boton derecha/izquierda
UD=0.0  #Boton UP/DOWN
SQ=0.0
SR=0.0
p_x = []
p_y = []
W=0.0
T=W
y=0.0
S=y
alpha=0.45
xp=0.0
xpt=0.0
yp=0.0
counter=1
counter1=1
k=0
j=0
stop=0
capt=0
von=0
voff=0
#--------------------------------------------------------------
def Capturar(data):
    global capt
    capt=data.data
    print(capt)
    return capt

def VideoOn(data):
    global von
    von=data.data
    print(von)
    return von

def VideoOff(data):
    global voff
    voff=data.data
    print(voff)
    return voff

def talker():
    
    pub = rospy.Publisher('/webcam' , Image, queue_size = 1)
   
    #while not rospy.is_shutdown():
    
    msg = bridge.cv2_to_imgmsg(img , "bgr8")
    pub.publish(msg)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()


def talker2():
    
    pub = rospy.Publisher('position_state_x' , Float32, queue_size = 1)
    global x,i,p_x,S,y, alpha, xp,xpt,stop#,k, counter
    #while not rospy.is_shutdown():
    if x_medium>=0 and x_medium<=640 and  y_medium>=0 and y_medium<480:
       
        x_position=x_medium
        
        print(stop)
        S=(alpha*x_position)+((1-alpha)*S)
        print("FILTRO: ", S)
        xp=S-320
        #xpt=S+xp
        print(xp)
        #print(xpt)
        #p_x.append(x_position)
        #if xp>50 and counter==1:
        #    k=40
        #    counter=0
        #if xp<50 and counter==1:
        #    k=20
        #    counter=0

        i+=1

        if i==40 and xp>-20 and xp<=0 or  i==40 and xp>=0 and xp<20:
            i=0
            print(stop)

        if i==40 and xp<=-20   or i==40 and xp>=20 :
            print(stop)
        #    x=sum(p_x)/i
        #    print(x)
            i=0
            rospy.loginfo(S)
            pub.publish(S)
            #counter=1
        #del p_x[:]

    else:
        x_position=320
        rospy.loginfo(x_position)
        pub.publish(x_position)
    

def talker3():
    global u,p_y,T,W, alpha,yp,stop #, counter1,j, yp
    pub = rospy.Publisher('position_state_y' , Float32, queue_size = 1)
    
    #while not rospy.is_shutdown():
    
    if x_medium>=0 and x_medium<=640 and  y_medium>=0 and y_medium<480:
        print(stop)
        y_position=y_medium
       
        T=(alpha*y_position)+((1-alpha)*T) 
        yp=T-240
        print(T)
        print(yp)
        print("FILTRO: ", T)

        #p_y.append(y_position)
        #if yp>50 and counter1==1:
        #    j=40
        #    counter1=0
        #if yp<50 and counter1==1:
        #    j=20
        #    counter1=0

        u+=1
        
        if u==40 and yp>-20 and yp<=0 or  u==40 and yp>=0 and yp<20:
            u=0
            #z=sum(p_y)/u
            #print(z)
        if u==40 and yp<=-20  or u==40 and yp>=20 :
            u=0
            rospy.loginfo(T)
            pub.publish(T) 
            #counter1=1
            #del p_y[:]
    else:
        y_position=240
        rospy.loginfo(y_position)
        pub.publish(y_position)

#def callback3(data):
    #global stop
    #stop=data.data
   # print("Llego un dato")
   # print(stop)
  # return stop

def callback2(data):
    global A,B,X,Y,RB,LB,UD,DI,SQ, SR,LT
    A=data.buttons[0]  #Obtencion de los datos de los botones del control xbox
    B=data.buttons[1]
    X=data.buttons[2]
    Y=data.buttons[3]
    RB=data.buttons[5]
    LB=data.buttons[4]
    UD=data.axes[7]
    DI=data.axes[6]
    LB=data.axes[5]
    LT=data.axes[2]
    SQ=data.buttons[6]
    SR=data.buttons[7]
    
    return A,B,X,Y,RB,LB,UD,DI,SQ


def photo():
    global img_counter
    img_name = "imagen_{}.png".format(img_counter) 
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name)) 
    img_counter += 1  


def video():
    
    global vi_counter,salida, vid
    if vid==0:
        codecs = cv2.VideoWriter_fourcc(*'MP4V')
        salida = cv2.VideoWriter('video_{}.mp4'.format(vi_counter),codecs,20.0,(640,480))
        vi_counter+=1
        vid=1
     


       


frameWidth=640
frameHeight=480
cap = cv2.VideoCapture(2)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
x_medium = int(640 / 2)
y_medium = int(480 / 2)
center = int(480 / 2)
position = 90
linea=0
ret,img = cap.read()

def empty(a):
    pass
def dempty(b):
    pass

rospy.init_node('image' , anonymous = False)

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
ower_blue = np.array([h_mi, s_mi, v_mi])
upper_blue = np.array([h_ma, s_ma, v_ma])
kernel = np.ones((kmi, kma), np.uint8)
okernel = np.ones((okmi, okma), np.uint8)
erosion = cv2.erode(hsv, kernel, iterations=it)
dilation = cv2.dilate(erosion, kernel, iterations=itd)


while True:
    ret,img = cap.read()
    ret,frame= cap.read()
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
    # yellow
    # lower_blue = np.array([34, 116, 111])
    # upper_blue = np.array([72, 255, 255])
    # kernel = np.ones((3,3), np.uint8)
    # okernel = np.ones((0, 0), np.uint8)
    # erosion = cv2.erode(hsv, kernel, iterations=3)
    # dilation = cv2.dilate(erosion, kernel, iterations=3)
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
    # imgray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
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
        # print(cnt)
        # M = cv2.moments(cnt)
        # print(M)
        # cx = int(M['m10'] / M['m00'])
        # cy = int(M['m01'] / M['m00'])
        area = cv2.contourArea(cnt)
        #print("area is: " + str(area))
        perimeter = cv2.arcLength(cnt, True)
        #print("perimeter is: " + str(perimeter))

        epsilon = 0.1 * cv2.arcLength(cnt, True)
        # print("elipson is: "+ str(epsilon))
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        # print("approx is: " +str(approx))
        area_approx = cv2.contourArea(approx)
        #print("area_approx is: " + str(area_approx))
        hull = cv2.convexHull(cnt)
        area_hull = cv2.contourArea(hull)
        #print("area_hull is: " + str(area_hull))
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
    #cv2.imshow("thresh",thresh)
    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    #contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #contours = imutils.grab_contours(contours)
    
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
    
    
    if x_medium < center - 30:
            position += 1
    elif x_medium > center + 30:
            position -= 1
    print(center)
    print("X_position is: ",x_medium)
    print("Y_position is: ",y_medium)

    print("position is: " + str(position))
    cv2.imshow("Original",img)
    #rospy.Subscriber('stop', Float32, callback3)

    #talker()
    talker2()
    talker3()
    rospy.Subscriber('Capturar', Float32, Capturar)
    rospy.Subscriber('VideoOn', Float32, VideoOn)
    rospy.Subscriber('VideoOff', Float32, VideoOff)
    if capt==1:
       photo()
    
    if von==1:
       video()

    if vid==1:
     salida.write(frame)

    if voff==1:
        vid=0
    
   # _.img= im.read(cv2.VideoCapture("http://192.168.0.172:8080/video"))
   
    #cv2.imshow("thresh", thresh)
    #blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
     
    #GPIO.output(SEÑAL1,0)
    #GPIO.output(SEÑAL2,0)   
           
    if x_medium>=280 and x_medium<=350: #ESTANDAR 300,330
       print("OBJECT FOUND")
       #zePIO.output(SEÑAL1,1)
       
 #     if x_medium>=150 and x_medium<=450:
 #        print("OBJECT IN FRAME")
 #        GPIO.output(SEÑAL2,1)
       
    else:
       print("SEARCHING OBJECT")
       #GPIO.output(SEÑAL1,0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        

