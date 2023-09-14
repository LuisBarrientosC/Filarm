#!/usr/bin/python3

#https://aniekan.blog/2022/01/24/creating-your-first-package-in-ros/
#http://wiki.ros.org/ROS/Tutorials/CreatingPackage
#http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
#http://wiki.ros.org/ROS/Tutorials/ExaminingPublisherSubscriber


## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

print("Talker running")
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass