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
from std_msgs.msg import String, Float32, Float32MultiArray
from moveit_commander.conversions import pose_to_list
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

def planear3():
    
    global M6,M5, BUSY 
    BUSY=True                                              
    print('Entre a la funcion planear(x,y)')
    # We can get the joint values from the group and adjust some of the values:
    joint_goal = move_group.get_current_joint_values()
    print(joint_goal)

    # joint_goal[1] = 0
    # joint_goal[2] = 0
    # joint_goalint_goal[5] = M6[3] = 0
    # joint_goal[4] = 0
    # joint_goal[5] = 0
    # joint_goal[6] = 0

    #cambiar joint values
    
    joint_goal[4] = M5
    joint_goal[5] = M6 #  // radians

    # The go command can be called with joint values, poses, or without any
    # parameters if you have already set the pose or joint target for the group
    
    move_group.set_joint_value_target(joint_goal)
    plan = move_group.go( wait=False)
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
    rospy.sleep(5)
    BUSY=False                                            
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
    counter=0
    S=1
    try:

        while S==1:
       	        counter +=1
		if counter==1:
		    M6+=0.5
		    planear3()

		if counter==2:
		    M6-=0.5
		    counter=0
		    planear3()

		
        rospy.spin()
           
    except rospy.ROSInterruptException:
        pass
