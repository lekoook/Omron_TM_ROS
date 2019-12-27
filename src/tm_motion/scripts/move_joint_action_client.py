#! /usr/bin/env python
import rospy
import actionlib
from tm_motion.msg import ActionAction, ActionGoal

def feedback_cb(msg):
 print 'Feedback received:', msg

def call_server():

    client = actionlib.SimpleActionClient('move_joint', ActionAction)

    client.wait_for_server()

    goal = ActionGoal()
    goal.goal_goal = j1, j2, j3, j4, j5, j6

    client.send_goal(goal, feedback_cb=feedback_cb)

    client.wait_for_result()

    result = client.get_result()

    return result

if __name__ == '__main__':
    if len(sys.argv) == 7:
        j1 = str(sys.argv[1])
        j2 = str(sys.argv[2])
        j3 = str(sys.argv[3])
        j4 = str(sys.argv[4])
        j5 = str(sys.argv[5])
        j6 = str(sys.argv[6])
    else:
        print usage()
        sys.exit(1)
    try:
        rospy.init_node('move_joint_action_client')
        result = call_server()
        print 'The result is:', result
    except rospy.ROSInterruptException as e:
        print 'Something went wrong:', e
