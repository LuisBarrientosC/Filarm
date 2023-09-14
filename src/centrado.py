#!/usr/bin/python

from __future__ import print_function
# from six.moves import input

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String, Float32
from moveit_commander.conversions import pose_to_list
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy


M5=0.0
M6=0.0

def callback(data):
    
    global M5
    global M6
    global xp
	    

    xp=data.data
    xpi= 320-xp
    print(xpi)

    if xpi < -15 and xpi>-50:
        M6 +=0.03 #RAD
        planear()

    if xpi < -50:
        M6 +=0.06 #RAD
        planear()

    if xpi> 15 and xpi < 50 :
        M6 -=0.03
        planear()

    if xpi> 50 :
        M6 -=0.06
        planear()
    
    return xp, M6

def callback1(data):


	global M5
	global yp

	yp=data.data
	    
	ypi= 240-yp
	print(ypi)
	    
	    
	if ypi < -20 and ypi>-100: #and M3 != 2 and M2<=1.4:
			M5 -=0.01 #RAD
			planear2()
	if ypi < -100: #and M3 != 2 and M2<=1.4:
			M5 -=0.01 #RAD
			planear2()
		#if M3==2:
		#	while M3 >= 0.5 and ypi < -20 and M2 <= 1.4 : 
		#		M2 +=0.02 #RAD
		#		M3 -=0.02 #RAD
	        #                planear()

	if ypi > 20 and ypi < 100  : #and M2 != -1 and M3< 1:
			M5 +=0.01 #RAD
			planear2()

	if ypi > 100: #and M2 != -1 and M3< 1:
			M5 +=0.01 #RAD
			planear2()

	        #if M2==0.8:
	        #        while M2 >= -1 and ypi > 20 and M3 <= 1 : 
                #        	M3 +=0.02 #RAD
	        #                M2 -=0.02 #RAD
	        #                planear()
	return yp,M5

def planear():
    

    
    global M6
    print('Entre a la funcion planear(x)')
    # We can get the joint values from the group and adjust some of the values:
    joint_goal = move_group.get_current_joint_values()
    print(joint_goal)

    # joint_goal[1] = 0
    # joint_goal[2] = 0
    # joint_goal[3] = 0
    # joint_goal[4] = 0
    # joint_goal[5] = 0
    # joint_goal[6] = 0

    #cambiar joint values
    
    
    joint_goal[5] = M6 #  // radians

    # The go command can be called with joint values, poses, or without any
    # parameters if you have already set the pose or joint target for the group
    move_group.set_joint_value_target(joint_goal)
    plan = move_group.go( wait=True)
    #plan = move_group.go(joint_goal, wait=True)
    print("after planning")
    # Calling ``stop()`` ensures that there is no residual movement
    move_group.stop()
    #joint_goal[0] =1.57  #;  // radians
    #joint_goal[1] = 0.0 #;  // radians
    #joint_goal[2] = 0.0 #;  // radians
    #joint_goal[3] = 0.0 #  // radians
    #joint_goal[4] = 0.0 #;  // radians
    #joint_goal[5] = 0.0 #;  // radians
    #move_group.execute(plan,  wait=True)
    #move_group.set_joint_value_target(joint_goal)
    # plan = move_group.go( wait=True)
    #rospy.sleep()                                                 
    print("end")

def planear2():
    

    global M5
   
    print('Entre a la funcion planear(Y)')
    # We can get the joint values from the group and adjust some of the values:
    joint_goal = move_group.get_current_joint_values()
    print(joint_goal)

    # joint_goal[1] = 0
    # joint_goal[2] = 0
    # joint_goal[3] = 0
    # joint_goal[4] = 0
    # joint_goal[5] = 0
    # joint_goal[6] = 0

    #cambiar joint values

    joint_goal[4] = M5 #  // radians
    
    # The go command can be called with joint values, poses, or without any
    # parameters if you have already set the pose or joint target for the group
    move_group.set_joint_value_target(joint_goal)
    plan = move_group.go( wait=True)
    #plan = move_group.go(joint_goal, wait=True)
    print("after planning")
    # Calling ``stop()`` ensures that there is no residual movement
    move_group.stop()
    #joint_goal[0] =1.57  #;  // radians
    #joint_goal[1] = 0.0 #;  // radians
    #joint_goal[2] = 0.0 #;  // radians
    #joint_goal[3] = 0.0 #  // radians
    #joint_goal[4] = 0.0 #;  // radians
    #joint_goal[5] = 0.0 #;  // radians
    #move_group.execute(plan,  wait=True)
    #move_group.set_joint_value_target(joint_goal)
    # plan = move_group.go( wait=True)
    rospy.sleep(0.5)                                                 
    print("end")


if __name__ == '__main__':

    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('robot_plan', anonymous=True)
    rospy.loginfo("robot_plan") 

    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()

    group_name = "manipulator"
    move_group = moveit_commander.MoveGroupCommander(group_name)

    #display_trajectory_publisher = rospy.Publisher('/ar3/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)
    # ar3/controllers/position
    # display_trajectory_publisher = rospy.Publisher(
    #     "/display_planned_path", moveit_msgs.msg.DisplayTrajectory, queue_size=20
    # )

    # We can get the name of the reference frame for this robot:
    planning_frame = move_group.get_planning_frame()
    print("============ Planning frame: %s" % planning_frame)

    # We can also print the name of the end-effector link for this group:
    eef_link = move_group.get_end_effector_link()
    print("============ End effector link: %s" % eef_link)

    # We can get a list of all the groups in the robot:
    group_names = robot.get_group_names()
    print("============ Available Planning Groups:", robot.get_group_names())

    # Sometimes for debugging it is useful to print the entire state of the
        # robot:
    print("============ Printing robot state")
    print(robot.get_current_state())
    print("")
    joint_goal = move_group.get_current_joint_values()
    M5=  joint_goal[4]
    M6=  joint_goal[5]  
    try:
        rospy.Subscriber('position_state_x', Float32, callback)
        #rospy.Subscriber('position_state_y', Float32, callback1)
        rospy.spin()
           
    except rospy.ROSInterruptException:
        pass
