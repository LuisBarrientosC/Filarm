#!/usr/bin/python3


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


moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('robot test', anonymous=True)
rospy.loginfo("Robot test")

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
joint_goal[0] =0 #1.57  #;  // radians
joint_goal[1] = 0.785 #;  // radians
joint_goal[2] = 1.57 #;  // radians
joint_goal[3] = 0.0 #  // radians
joint_goal[4] = -0.785 #;  // radians
joint_goal[5] = 0.0 #;  // radians


#move_group.set_max_acceleration_scaling_factor(2)
#move_group.set_max_velocity_scaling_factor(2)
# The go command can be called with joint values, poses, or without any
# parameters if you have already set the pose or joint target for the group
move_group.set_max_acceleration_scaling_factor(1)
move_group.set_max_velocity_scaling_factor(1)
move_group.set_joint_value_target(joint_goal)
#plan = move_group.go( wait=True)
plan = move_group.go(joint_goal, wait=True)
#print("after planning")
# Calling ``stop()`` ensures that there is no residual movement
move_group.stop()
#rospy.sleep(10)
joint_goal[0] =1.57  #;  // radians
joint_goal[1] = 0.0 #;  // radians
joint_goal[2] = 0.0 #;  // radians
joint_goal[3] = 0.0 #  // radians
joint_goal[4] = 0.0 #;  // radians
joint_goal[5] = 0.0 #;  // radians
# move_group.execute(plan,  wait=True)
#move_group.set_max_acceleration_scaling_factor(0.1)
#move_group.set_max_velocity_scaling_factor(0.1)
move_group.set_joint_value_target(joint_goal)
plan = move_group.go( wait=True)
#plan = move_group.go(wait=True)
# Calling `stop()` ensures that there is no residual movement
move_group.stop()
# It is always good to clear your targets after planning with poses.
# Note: there is no equivalent function for clear_joint_value_targets()
#rospy.sleep(10)
print("end")