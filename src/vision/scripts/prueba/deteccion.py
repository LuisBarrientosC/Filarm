#!/usr/bin/env python
import sys
import rospy
import cv2

def main():

 if len(sys.argv) <2:
   print ("Usage: tracker <algorithm name>")
   sys.exit()

 rospy.init_node('tracker', anonymous=True) 
 #Create & tracker object
 # Pssible algratas, DUSTIN, KEP, FL LOW (31)

 tracker= cv2.TrackerKCF_create(sys.argv[1])
 cap= cv2.VideoCapture(2)  

 if not cap.isOpened():
   print ("Unable to open default camera device")
   sys.exit()


 cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320);
 cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240);
 cap.set(cv2.CAP_PROP_FPS, 10);

 ok, frame=cap.read() 

 if not ok:
   print ('Cannot read camera file')
   sys.exit()

 bbox= cv2.selectROI(frame, False)

 cv2.destroyAllWindows()
 #hipotire tracker bath first frame and bounding box 
 ok= tracker.init(frame, bbox)

 #Perfore the tracking process 

 print ("start the tracking process, press CTRL+C to quit.") 
 rate= rospy.Rate(10)

 while not rospy.is_shutdown():

   #frame from the ca 
   ok, frame= cap.read()

   #Stop the are

   if not ok: 
      break

   #te the fracking restt 
   ok, bbox= tracker.update (frame)

   #the tracked on fact

   if ok: 
     p1= (int(bbox[0]), int(bbox=[1]))
     p2= (int(bbox[0]+ bbox[2]), int (bbox[1]+ bbox[3]))
     cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)


    #show image it the tracked inject
   cv2.imshow("Tracking",frame)

    #still nent witty

   cv2.waitKey(1)

   rate.sleep()

if __name__ == '__main__':
    try:
      main()
    except rospy.ROSInterruptException:
      pass

