#!/usr/bin/python3

#https://aniekan.blog/2022/01/24/creating-your-first-package-in-ros/
#http://wiki.ros.org/ROS/Tutorials/CreatingPackage
#http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
#http://wiki.ros.org/ROS/Tutorials/ExaminingPublisherSubscriber

#https://www.theconstructsim.com/ros-qa-138-how-to-set-a-sequence-of-goals-in-moveit-for-a-manipulator/


## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import String


print("Talker running")
