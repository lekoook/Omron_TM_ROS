#!/usr/bin/env python
import sys
import rospy
from tm_motion.srv import *
import actionlib
from tm_motion.msg import ActionAction, ActionGoal

def landmark_location_service_client():
    global nc
    rospy.wait_for_service('landmark_location')
    try:
        service = rospy.ServiceProxy('landmark_location', TmMotion)
        resp1 = service()
        nc  = resp1.device
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def feedback_cb(msg):
 print 'Feedback received:', msg

def call_server():
    client = actionlib.SimpleActionClient('move_action', ActionAction)
    client.wait_for_server()
    goal = ActionGoal()
    # goal.goal_goal1 = vision_x
    # goal.goal_goal2 = vision_y
    # goal.goal_goal3 = vision_z
    # goal.goal_goal4 = vision_Rx
    # goal.goal_goal5 = vision_Ry
    # goal.goal_goal6 = vision_Rz
    client.send_goal(goal, feedback_cb=feedback_cb)
    client.wait_for_result()
    result = client.get_result()
    return result


if __name__ == "__main__":
    print landmark_location_service_client()
    vision_x = nc.partition("\\")[0]
    vision_y = nc.partition("\\\\")[0].replace(vision_x, '').replace('\\', '')
    vision_z = nc.partition("\\\\\\")[0].replace(vision_x, '').replace(vision_y, '').replace('\\', '')
    vision_Rx = nc.partition("\\\\\\\\")[0].replace(vision_x, '').replace(vision_y, '').replace(vision_z, '').replace('\\', '')
    vision_Ry = nc.partition("\\\\\\\\\\")[0].replace(vision_x, '').replace(vision_y, '').replace(vision_z, '').replace(vision_Rx, '').replace('\\', '')
    vision_Rz = nc.replace(vision_x, '').replace(vision_y, '').replace(vision_z, '').replace(vision_Rx, '').replace(vision_Ry, '').replace('\\', '')
    print float(vision_x)
    print float(vision_y)
    print float(vision_z)
    print float(vision_Rx)
    print float(vision_Ry)
    print float(vision_Rz)
    try:
        rospy.init_node('move_action_client')
        goal = ActionGoal()
        goal.goal_goal1 = float(vision_x)
        goal.goal_goal2 = float(vision_y)+100
        goal.goal_goal3 = float(vision_z)+350
        goal.goal_goal4 = float(vision_Rx)
        goal.goal_goal5 = float(vision_Ry)
        goal.goal_goal6 = float(vision_Rz)-180
        result = call_server()
        print 'The result is:', result
    except rospy.ROSInterruptException as e:
        print 'Something went wrong:', e
