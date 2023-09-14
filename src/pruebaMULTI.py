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
import multiprocessing

global M1,M2,M3,M6
l=0
M6=0.0
def T2():
     global M6
     M6 +=0.01
     p2=multiprocessing.Process(target=planear1)
     p2.start()
     
def callback(data):

    global M6
    global xp,op,counter
	    
    
    counter=1
    xp=data.data
   # y = _map(xp, 0, 640,-2.29, 2.29)
    #print(y)

    xpi= 320-xp
    print(xpi)
   
    if op==0 and counter==1:       
         
        if xpi < -15 and xpi>-50:
                xpii= -((xpi*0.01)/7)
                M6 += xpii
                print(M6)
                p2.start()
                p2.join()

        if xpi < -50:
                M6 += -((xpi*0.01)/7)
                print(M6)
                p2.start()
                p2.join()

        if xpi> 15 and xpi < 50 :
                M6 += -((xpi*0.01)/7)
                print(M6)
                p2.start()
                p2.join()

        if xpi> 50 :
                
                M6 += -((xpi*0.01)/7)
                print(M6)  
                p2.start()
                p2.join() 
    
    return xp, M6

def planear1():

    global M6,op, counter
    op=1
    print(op) 
    #talker()                                                
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
    
    
    joint_goal[5] = float(M6) #  // radians

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
    rospy.sleep(3)
    op=0
    counter=0
    print(op)                                                 
    print("end")
    #talker()

def trayectoria():
    global M1,M2,M3

    M1 = 0.676067943799
    M2 = 6.13592315155e-05
    M3 = 1.47513728486
    #p1=multiprocessing.Process(target=plano)
    #p1.start()
    plano()
    

    M1 = 0.0
    M2 = 0.000368155389093
    M3 = 1.47532136256
    #p1=multiprocessing.Process(target=plano)
    #p1.start()
    plano()
    

    M1 =-0.779142930629
    M2 = 6.13592315155e-05
    M3 = 1.47513728486
    #p1=multiprocessing.Process(target=plano)
    #p1.start()
    plano()
    

def plano():
    global M1,M2,M3    
    print('Entre a la funcion planear')
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
    joint_goal[0] = float(M1)    #  // radians
    joint_goal[1] = float(M2)   #  // radians-0.6   1.37
    joint_goal[2] = float(M3)  #  // radians 0 2.5
    
    # The go command can be called with joint values, poses, or without any
    # parameters if you have already set the pose or joint target for the group
    move_group.set_max_acceleration_scaling_factor(0.5)
    move_group.set_max_velocity_scaling_factor(0.5)
    move_group.set_joint_value_target(joint_goal)
    plan = move_group.go( wait=False)
    #plan = move_group.go(joint_goal, wait=True)
    print("after planning")
    # Calling ``stop()`` ensures that there is no residual movement
    move_group.stop()
    T2()
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
    M1=  joint_goal[0]
    M2=  joint_goal[1]
    M3=  joint_goal[2]
    M4=  joint_goal[3]
    M5=  joint_goal[4]
    M6=  joint_goal[5] 

    #p1=multiprocessing.Process(target=plano)
    #p1.start()
    #p2=multiprocessing.Process(target=planear1, args =M6)
    try:
        rospy.Subscriber('position_state_x', Float32, callback)
        #rospy.Subscriber('position_state_y', Float32, callback1)
        while (l<10): 
         trayectoria()
         
         l+=1
        #rospy.spin()
           
    except rospy.ROSInterruptException:
        pass
