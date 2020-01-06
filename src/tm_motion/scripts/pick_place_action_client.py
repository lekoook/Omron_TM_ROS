#! /usr/bin/env python
import rospy
import actionlib
import sys
from tm_motion.msg import ActionAction, ActionGoal

def feedback_cb(msg):
 print 'Feedback received:', msg

def call_server():

    client = actionlib.SimpleActionClient('move_joint', ActionAction)

    client.wait_for_server()

    goal = ActionGoal()
    goal.goal_goal1 = ""

    client.send_goal(goal, feedback_cb=feedback_cb)

    client.wait_for_result()

    result = client.get_result()

    return result


if __name__ == '__main__':
    try:
        rospy.init_node('move_joint_action_client')
        result = call_server()
        print 'The result is:', result
    except rospy.ROSInterruptException as e:
        print 'Something went wrong:', e
