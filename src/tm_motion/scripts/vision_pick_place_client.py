#!/usr/bin/env python
import sys
import rospy
import time
from tm_motion.srv import *
import actionlib
from tm_motion.msg import ActionAction, ActionGoal
from pymodbus.client.sync import ModbusTcpClient
import tf
import tf2_ros
import geometry_msgs.msg
import math
host = '192.168.1.2'
port_modbus = 502
client = ModbusTcpClient(host, port_modbus)
client.connect()

def start_program():
    print "starting program"
    status = client.write_coil(7104, True, unit=1)
    print(status)
    time.sleep(5)

def stop_program():
    print "stopping program"
    status = client.write_coil(7105, True, unit=1)
    print(status)
    time.sleep(2)

def grip():
    print "griping object"
    #go into gipper function
    status = client.write_coil(0003, False, unit=1)
    print(status)
    status = client.write_coil(0002, True, unit=1)
    print(status)
    time.sleep(1)
    status = client.write_coil(0000, True, unit=1)
    time.sleep(1)

def release():
    #go into gipper function
    status = client.write_coil(0002, True, unit=1)
    print(status)
    time.sleep(1)
    #open gripper
    print "opening gripper"
    status = client.write_coil(0001, True, unit=1)
    time.sleep(0.5)

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
    client.send_goal(goal, feedback_cb=feedback_cb)
    client.wait_for_result()
    result = client.get_result()
    return result

if __name__ == "__main__":
    rospy.init_node('test_tf')

    print "moving to initial location to scan tm landmark"
    try:
        goal = ActionGoal()
        goal.goal_goal1 = -326.47
        goal.goal_goal2 = -53.09
        goal.goal_goal3 = 646.33
        goal.goal_goal4 = -177.09
        goal.goal_goal5 = -1.64
        goal.goal_goal6 = -90.20
        result = call_server()
        print 'The result is:', result
    except rospy.ROSInterruptException as e:
        print 'Something went wrong:', e

    print "scanning for tm landmark location"
    print landmark_location_service_client()
    rate = rospy.Rate(10.0)
    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)
    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform('base_link', 'landmark_location', rospy.Time())
            print trans.transform
            break
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue

    broadcaster2 = tf2_ros.StaticTransformBroadcaster()
    landmark_to_obj = geometry_msgs.msg.TransformStamped()
    landmark_to_obj.header.stamp = rospy.Time.now()
    landmark_to_obj.header.frame_id = "landmark_location"
    landmark_to_obj.child_frame_id = "object_location"
    landmark_to_obj.transform.translation.x = 100
    landmark_to_obj.transform.translation.y = 0
    landmark_to_obj.transform.translation.z = -350
    quat = tf.transformations.quaternion_from_euler(
               0,0,-math.pi)
    landmark_to_obj.transform.rotation.x = quat[0]
    landmark_to_obj.transform.rotation.y = quat[1]
    landmark_to_obj.transform.rotation.z = quat[2]
    landmark_to_obj.transform.rotation.w = quat[3]
    broadcaster2.sendTransform(landmark_to_obj)
    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform('base_link', 'object_location', rospy.Time())
            print "new values:"
            print trans.transform
            break
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue
    quaternion = (
    trans.transform.rotation.x,
    trans.transform.rotation.y,
    trans.transform.rotation.z,
    trans.transform.rotation.w)
    euler = tf.transformations.euler_from_quaternion(quaternion)
    Rx = math.degrees(euler[0])
    Ry = math.degrees(euler[1])
    Rz = math.degrees(euler[2])
    print trans.transform.translation.x
    print trans.transform.translation.y
    print trans.transform.translation.z
    print Rx
    print Ry
    print Rz

    start_program()
    release()
    stop_program()

    try:
        goal = ActionGoal()
        goal.goal_goal1 = trans.transform.translation.x
        goal.goal_goal2 = trans.transform.translation.y
        goal.goal_goal3 = trans.transform.translation.z
        goal.goal_goal4 = Rx
        goal.goal_goal5 = Ry
        goal.goal_goal6 = Rz
        result = call_server()
        print 'The result is:', result
        print "moved to pickup location"
    except rospy.ROSInterruptException as e:
        print 'Something went wrong:', e

    start_program()
    grip()
    print "gripped object"
    stop_program()

    try:
        goal = ActionGoal()
        goal.goal_goal1 = trans.transform.translation.x
        goal.goal_goal2 = trans.transform.translation.y
        goal.goal_goal3 = trans.transform.translation.z + 100
        goal.goal_goal4 = Rx
        goal.goal_goal5 = Ry
        goal.goal_goal6 = Rz
        result = call_server()
        print 'The result is:', result
    except rospy.ROSInterruptException as e:
        print 'Something went wrong:', e

    print "moving to dropoff location to scan tm landmark"
    try:
        goal = ActionGoal()
        goal.goal_goal1 = -202
        goal.goal_goal2 = 530.38
        goal.goal_goal3 = 437.76
        goal.goal_goal4 = 179.13
        goal.goal_goal5 = -0.58
        goal.goal_goal6 = -87.82
        result = call_server()
        print 'The result is:', result
    except rospy.ROSInterruptException as e:
        print 'Something went wrong:', e

    print "scanning for tm landmark location"
    print landmark_location_service_client()
    rate = rospy.Rate(10.0)
    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)
    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform('base_link', 'landmark_location', rospy.Time())
            print trans.transform
            break
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue

    broadcaster2 = tf2_ros.StaticTransformBroadcaster()
    landmark_to_obj = geometry_msgs.msg.TransformStamped()
    landmark_to_obj.header.stamp = rospy.Time.now()
    landmark_to_obj.header.frame_id = "landmark_location"
    landmark_to_obj.child_frame_id = "place_location"
    landmark_to_obj.transform.translation.x = 100
    landmark_to_obj.transform.translation.y = 0
    landmark_to_obj.transform.translation.z = -250
    quat = tf.transformations.quaternion_from_euler(
               0,0,-math.pi)
    landmark_to_obj.transform.rotation.x = quat[0]
    landmark_to_obj.transform.rotation.y = quat[1]
    landmark_to_obj.transform.rotation.z = quat[2]
    landmark_to_obj.transform.rotation.w = quat[3]
    broadcaster2.sendTransform(landmark_to_obj)
    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform('base_link', 'place_location', rospy.Time())
            print "place location:"
            print trans.transform
            break
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue
    quaternion = (
    trans.transform.rotation.x,
    trans.transform.rotation.y,
    trans.transform.rotation.z,
    trans.transform.rotation.w)
    euler = tf.transformations.euler_from_quaternion(quaternion)
    Rx = math.degrees(euler[0])
    Ry = math.degrees(euler[1])
    Rz = math.degrees(euler[2])
    print trans.transform.translation.x
    print trans.transform.translation.y
    print trans.transform.translation.z
    print Rx
    print Ry
    print Rz

    try:
        goal = ActionGoal()
        goal.goal_goal1 = trans.transform.translation.x
        goal.goal_goal2 = trans.transform.translation.y
        goal.goal_goal3 = trans.transform.translation.z
        goal.goal_goal4 = Rx
        goal.goal_goal5 = Ry
        goal.goal_goal6 = Rz
        result = call_server()
        print 'The result is:', result
        print "moved to dropoff location"
    except rospy.ROSInterruptException as e:
        print 'Something went wrong:', e

    start_program()
    release()
    stop_program()
