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
    print "scanning for tm landmark location"
    print landmark_location_service_client()
    # vision_x = nc.partition("\\")[0]
    # vision_y = nc.partition("\\\\")[0].replace(vision_x, '').replace('\\', '')
    # vision_z = nc.partition("\\\\\\")[0].replace(vision_x, '').replace(vision_y, '').replace('\\', '')
    # vision_Rx = nc.partition("\\\\\\\\")[0].replace(vision_x, '').replace(vision_y, '').replace(vision_z, '').replace('\\', '')
    # vision_Ry = nc.partition("\\\\\\\\\\")[0].replace(vision_x, '').replace(vision_y, '').replace(vision_z, '').replace(vision_Rx, '').replace('\\', '')
    # vision_Rz = nc.replace(vision_x, '').replace(vision_y, '').replace(vision_z, '').replace(vision_Rx, '').replace(vision_Ry, '').replace('\\', '')
    # print float(vision_x)
    # print float(vision_y)
    # print float(vision_z)
    # print float(vision_Rx)
    # print float(vision_Ry)
    # print float(vision_Rz)
    rospy.init_node('tf2_listener')
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
    landmark_to_obj.transform.translation.x = 0
    landmark_to_obj.transform.translation.y = 100
    landmark_to_obj.transform.translation.z = 100
    quat = tf.transformations.quaternion_from_euler(
               0,0,0)
    landmark_to_obj.transform.rotation.x = quat[0]
    landmark_to_obj.transform.rotation.y = quat[1]
    landmark_to_obj.transform.rotation.z = quat[2]
    landmark_to_obj.transform.rotation.w = quat[3]
    broadcaster2.sendTransform(landmark_to_obj)
    trans = tfBuffer.lookup_transform('base_link', 'object_location', rospy.Time())
    print trans.transform

    # pick_location = trans.transform * landmark_to_obj.transform
    # print pick_location




    start_program()
    release()
    stop_program()
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
        print "moved to pickup location"
    except rospy.ROSInterruptException as e:
        print 'Something went wrong:', e
    start_program()
    grip()
    print "gripped object"
    stop_program()
    try:
        rospy.init_node('move_action_client')
        goal = ActionGoal()
        goal.goal_goal1 = float(vision_x)
        goal.goal_goal2 = float(vision_y)+100
        goal.goal_goal3 = float(vision_z)+450
        goal.goal_goal4 = float(vision_Rx)
        goal.goal_goal5 = float(vision_Ry)
        goal.goal_goal6 = float(vision_Rz)-180
        result = call_server()
        print 'The result is:', result
    except rospy.ROSInterruptException as e:
        print 'Something went wrong:', e
    time.sleep(1)
    print "scanning for tm landmark location"
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
        print "moved to dropoff location"
    except rospy.ROSInterruptException as e:
        print 'Something went wrong:', e
    start_program()
    release()
    stop_program()
