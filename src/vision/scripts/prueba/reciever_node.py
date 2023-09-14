#!/usr/bin/python3

import rospy
from std_msgs.msg import String,Float32

def callback(data):
    rospy.loginfo('x_position: %f', data.data)

def callback1(data):
    rospy.loginfo('y_position: %f', data.data)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously
    # anonymous=True flag means that rospy will choose a unique
    rospy.init_node('listener', anonymous=True) 

    rospy.Subscriber('position_state_x', Float32, callback)
    rospy.Subscriber('position_state_y', Float32, callback1)
    # spin() simply keeps python from exiting until this node is stopped
    # anonymous=True flag means that rospy will choose a unique
    rospy.spin()

if __name__ == '__main__':
    listener()
