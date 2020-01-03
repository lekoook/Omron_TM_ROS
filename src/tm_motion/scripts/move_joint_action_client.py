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
    goal.goal_function = function
    goal.goal_param = param
    goal.goal_goal1 = j1
    goal.goal_goal2 = j2
    goal.goal_goal3 = j3
    goal.goal_goal4 = j4
    goal.goal_goal5 = j5
    goal.goal_goal6 = j6

    client.send_goal(goal, feedback_cb=feedback_cb)

    client.wait_for_result()

    result = client.get_result()

    return result

def usage():
    return "please specify function, parameters and joint values <function> <parameters> <j1> <j2> <j3> <j4> <j5> <j6>"

if __name__ == '__main__':
    if len(sys.argv) == 9:
        function = str(sys.argv[1])
        param = str(sys.argv[2])
        j1 = str(sys.argv[3])
        j2 = str(sys.argv[4])
        j3 = str(sys.argv[5])
        j4 = str(sys.argv[6])
        j5 = str(sys.argv[7])
        j6 = str(sys.argv[8])
    else:
        print usage()
        sys.exit(1)
    try:
        rospy.init_node('move_joint_action_client')
        result = call_server()
        print 'The result is:', result
    except rospy.ROSInterruptException as e:
        print 'Something went wrong:', e
