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

xp=0.0
yp=0.0

global M1
global M2
global M3
global M4
global M5
global M6

CBX=0

A=0.0   
B=0.0
X=0.0
Y=0.0
RB=0.0
LB=0.0
DI=0.0  #Boton derecha/izquierda
UD=0.0  #Boton UP/DOWN
SQ=0.0

xbox_status=1
rviz_control=1
move=1

global i


M1=0.0
M2=0.0
M3=1.2
M4=0.0
M5=0.0
M6=0.0


def planear():
    
    global M1
    global M2
    global M3
    global M4
    global M5
    global M6,move
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
    joint_goal[0] = M1 #  // radians
    joint_goal[1] = M2 #  // radians
    joint_goal[2] = M3 #  // radians
    joint_goal[3] = M4 #  // radians
    joint_goal[4] = M5 #  // radians
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
    print("end")


def callback(data):
    global xp
    xp=data.data
    return xp

def callback1(data):
    global yp
    yp=data.data
    return yp

def callback2(data):
    global M1
    global M2
    global M3
    global M4
    global M5
    global M6,move
    global A,B,X,Y,RB,LB,UD,DI,SQ,xbox_status;
    A=data.buttons[0]  #Obtencion de los datos de los botones del control xbox
    B=data.buttons[1]
    X=data.buttons[2]
    Y=data.buttons[3]
    RB=data.buttons[5]
    LB=data.buttons[4]
    UD=data.axes[7]
    DI=data.axes[6]
    SQ=data.buttons[6]
    
    return A,B,X,Y,RB,LB,UD,DI,SQ

 
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('robot_plan', anonymous=True)
rospy.loginfo("robot_plan")
rospy.Subscriber("joy", Joy, callback2) 
rospy.Subscriber('position_state_x', Float32, callback)
rospy.Subscriber('position_state_y', Float32, callback1)



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

while True:
   
	while xbox_status==1:
		#CBX+=1
		#print("CXB", CBX)

		#rospy.Subscriber("joy", Joy, callback2) 

		if A==1 and DI==1 :           #Condiciones de los botones del xbox para 
		    M1+=0.1  #;  // radians   #establecer cuantos radianes se movera el robot. 
		    print("xbox_Control")
		    planear()
		     
		if A==1 and DI==-1 :
		    M1+=-0.1  #;  // radians
		    print("xbox_Control")
		    planear()

		if B==1 and UD==1 :
		    M2-=0.1  #;  // radians
		    print("xbox_Control")
		    planear()

		if B==1 and UD==-1 :
		    M2+=0.1  #;  // radians
		    print("xbox_Control")
		    planear()

		if Y==1 and UD==1 :
		    M3-=0.1  #;  // radians
		    print("xbox_Control")
		    planear()

		if Y==1 and UD==-1 :
		    M3+=0.1  #;  // radians
		    print("xbox_Control")
		    planear()

		if X==1 and DI==1 :
		    M4+=0.1 #;  // radians
		    print("xbox_Control")
		    planear()

		if X==1 and DI==-1 :
		    M4+=-0.1  #;  // radians
		    print("xbox_Control")
		    planear()

		if RB==1 and UD==1 :
		    M5-=0.1  #;  // radians
		    print("xbox_Control")
		    planear()

		if RB==1 and UD==-1 :
		    M5+=0.1  #;  // radians
		    print("xbox_Control")
		    planear()

		if LB==1 and DI==1 :
		    M6+=0.3  #;  // radians
		    print("xbox_Control")
		    planear()

		if LB==1 and DI==-1 :
		    M6+=-0.3  #;  // radians
		    print("xbox_Control")
		    planear()

		if SQ==1 and B==1:
		    xbox_status=0
		    print(xbox_status) 

		if move==1:
		   move=0
		   planear()


	while xbox_status==0 :

		print("Camera_control")


		xpi= 320-xp
		print(xpi)
		ypi= 240-yp
		print(ypi)

		print(M2)
		print(M3)


		if xpi < -20:
		    M1 +=0.01 #RAD

		if xpi > 20:
		    M1 -=0.01


		if ypi < -20 and M3 != 2 and M2<=1.4:
		    M3 +=0.01 #RAD
		    if M3==2:
		      while M3 >= 0.5 and ypi < -20 and M2 <= 1.4 : 
			M2 +=0.01 #RAD
			M3 -=0.01 #RAD

		if ypi > 20 and M2 != -1 and M3< 1:
			M2 -=0.01 #RAD
			if M2==0.8:
			    while M2 >= -1 and ypi > 20 and M3 <= 1 : 
				M3 +=0.01 #RAD
				M2 -=0.01 #RAD
		if SQ==1 and A==1:
		    xbox_status=1

		if SQ==1 and X==1:
		    rviz_control==1

		#if ypi > 20 and M3 != 1 :
		#   M3 -=0.05 #RAD

		#if ypi > 20 and M3 == 1:
		#   M2 -=0.05 #RAD



		# if ypi < 0.0:
		#    M2 +=0.1     #RAD

		# if ypi > 0.0:
		#     M2 -=0.1


		planear()



