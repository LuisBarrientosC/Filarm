#!/usr/bin/python
#encoding: utf-8

from __future__ import print_function
# from six.moves import input

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

#DEFINICION DE VARIABLES
#Botones control xbox
A=0.0   
B=0.0
X=0.0
Y=0.0
DI=0.0  #Boton derecha/izquierda
UD=0.0  #Boton UP/DOWN

#Variales de los Joints
M1=0.0
M2=0.0
M3=0.0
M4=0.0
M5=0.0
M6=0.0

def callback(data):

    global M1 #Globalizacion de las variales 
    global M2
    global M3
    global M4
    global M5
    global M6 
    
    A=data.buttons[0]  #Obtencion de los datos de los botones del control xbox
    B=data.buttons[1]
    X=data.buttons[2]
    Y=data.buttons[3]
    RB=data.buttons[5]
    LB=data.buttons[4]
    UD=data.axes[7]
    DI=data.axes[6]
    SQ=data.buttons[6]
    
    if A==1 and DI==1 :           #Condiciones de los botones del xbox para 
        M1+=0.1  #;  // radians   #establecer cuantos radianes se movera el robot. 
    if A==1 and DI==-1 :
        M1+=-0.1  #;  // radians
    
    if B==1 and UD==1 :
        M2+=0.1  #;  // radians
    if B==1 and UD==-1 :
        M2+=-0.1  #;  // radians
    
    if Y==1 and UD==1 :
        M3+=0.1  #;  // radians
    if Y==1 and UD==-1 :
        M3+=-0.1  #;  // radians
  
    if X==1 and DI==1 :
        M4+=0.1  #;  // radians
    if X==1 and DI==-1 :
        M4+=-0.1  #;  // radians

    if RB==1 and UD==1 :
        M5+=0.1  #;  // radians
    if RB==1 and UD==-1 :
        M5+=-0.1  #;  // radians

    if LB==1 and DI==1 :
        M6+=0.1  #;  // radians
    if LB==1 and DI==-1 :
        M6+=-0.1  #;  // radians
    
    if SQ==1 :
        print(joint_goal)
        # Calling ``stop()`` ensures that there is no residual movement
        move_group.stop()
        rospy.sleep(10)
        joint_goal[0] =1.57  #;  // radians
        joint_goal[1] = 0.0 #;   // radians
        joint_goal[2] = 0.0 #;   // radians
        joint_goal[3] = 0.0 #    // radians
        joint_goal[4] = 0.0 #;   // radians
        joint_goal[5] = 0.0 #;   // radians
        # move_group.execute(plan,  wait=True)
        move_group.set_joint_value_target(joint_goal)
        plan = move_group.go( wait=True)
        rospy.sleep(10)
        print("end") # Check si hay una excepción  Ctrl-C para terminar la ejecución del nodo
    
    #Visualizacion de los estados de los botones del control de xbox
    rospy.loginfo("JOY1X             %s", data.axes[0]) 
    rospy.loginfo("JOY1Y             %s", data.axes[1])
    rospy.loginfo("BUTTON LT         %s", data.axes[2])
    rospy.loginfo("JOY2X             %s", data.axes[3])
    rospy.loginfo("JOY2Y             %s", data.axes[4])
    rospy.loginfo("Button RT         %s", data.axes[5])
    rospy.loginfo("LEFT(+) RIGTH(-)  %s", DI)
    rospy.loginfo("DOWN(-) UP(+)     %s", UD)
    rospy.loginfo("Button A          %s", A)
    rospy.loginfo("Button B          %s", B)
    rospy.loginfo("Button X          %s", X)
    rospy.loginfo("Button Y          %s", Y)
    rospy.loginfo("Button LB         %s", LB)
    rospy.loginfo("Button RB         %s", RB)
    rospy.loginfo("Button SQ         %s", SQ)
    rospy.loginfo("Button LN         %s", data.buttons[7])
    rospy.loginfo("Button N/A        %s", data.buttons[8])
    rospy.loginfo("Button JOY1       %s", data.buttons[9])
    rospy.loginfo("Button JOY2       %s", data.buttons[10])
    rospy.loginfo("RADIANES J1       %s", M1) #visualizacion de los radianes recorridos por el robot
    rospy.loginfo("RADIANES J2       %s", M2)
    rospy.loginfo("RADIANES J3       %s", M3)
    rospy.loginfo("RADIANES J4       %s", M4)
    rospy.loginfo("RADIANES J5       %s", M5)
    rospy.loginfo("RADIANES J6       %s", M6)


    # We can get the joint values from the group and adjust some of the values:
    joint_goal = move_group.get_current_joint_values()
    #cambiar joint values
    joint_goal[0] = M1 #;  // radians
    joint_goal[1] = M2 #;  // radians
    joint_goal[2] = M3 #;  // radians
    joint_goal[3] = M4 #  // radians
    joint_goal[4] = M5 #;  // radians
    joint_goal[5] = M6 #;  // radians
    # The go command can be called with joint values, poses, or without any
    # parameters if you have already set the pose or joint target for the group
    move_group.set_joint_value_target(joint_goal)
    plan = move_group.go( wait=True)
    #plan = move_group.go(joint_goal, wait=True)
    print("after planning")

def nodo():
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('robot test', anonymous=True)
    rospy.loginfo("Robot test")
    rospy.Subscriber("joy", Joy, callback)  #Susbcripcion al rostopic JOY

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

    rospy.spin() 

 
if __name__ == '__main__':     #Llamamos a la función principal main
    try:
        robot = moveit_commander.RobotCommander()
        scene = moveit_commander.PlanningSceneInterface()
        group_name = "manipulator"
        move_group = moveit_commander.MoveGroupCommander(group_name)
        nodo()                  # LLamamos a la función nodo
    except rospy.ROSInterruptException: 
        # Calling ``stop()`` ensures that there is no residual movement
        pass


