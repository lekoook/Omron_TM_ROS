#!/usr/bin/env python
from pymodbus.client.sync import ModbusTcpClient
import struct
import time
import rospy
from ctypes import *
import socket
import subprocess
import os
from threading import Thread
from tm_motion.srv import TmMotion,TmMotionResponse
import tf
import tf2_ros
import geometry_msgs.msg
import math
ip_address = rospy.get_param("ip_address_tm")
# ip_address = '192.168.1.2'
port = 502
client = ModbusTcpClient(ip_address, port)
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

def utf8len(s):
    global length
    length = len(s.encode('utf-8'))
    return length

def getCheckSum(packet):
    global cs
    checksum = 0
    for el in packet:
        checksum ^= ord(el)
    cs = '{:02x}'.format(checksum)
    return cs
def socketconnect():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    print"socket timeout:" , s.gettimeout(),"s"
    print"connecting to tm robot......"

def check_server():
    ip_address = rospy.get_param("ip_address_tm")
    # ip_address = '192.168.1.2'
    #default port for listen node
    port = 5890
    try:
        s.connect((ip_address, port))
        print("Connected")

    except socket.error:
        print("Connection  failed. Did you run listen node?")
        exit(0)

def script_exit():
    socketconnect()
    check_server()
    utf8len("1,ScriptExit()".format())
    getCheckSum("TMSCT,{},1,ScriptExit(),".format(length))
    command =  "$TMSCT,{},1,ScriptExit(),*{}".format(length, cs)
    print "Running scriptExit:", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    BUFFER_SIZE = 1024
    data = s.recv(BUFFER_SIZE)
    rcv = data.decode("utf-8")
    print rcv

def vision():
    global vision_x, vision_y, vision_z, vision_Rx, vision_Ry, vision_Rz, nc
    #read tm landmark postion values
    nc = subprocess.check_output(["netcat", "-l", "9000", "-w", "1"])
    print nc
    vision_x = nc.partition("\\")[0]
    vision_y = nc.partition("\\\\")[0].replace(vision_x, '').replace('\\', '')
    vision_z = nc.partition("\\\\\\")[0].replace(vision_x, '').replace(vision_y, '').replace('\\', '')
    vision_Rx = nc.partition("\\\\\\\\")[0].replace(vision_x, '').replace(vision_y, '').replace(vision_z, '').replace('\\', '')
    vision_Ry = nc.partition("\\\\\\\\\\")[0].replace(vision_x, '').replace(vision_y, '').replace(vision_z, '').replace(vision_Rx, '').replace('\\', '')
    vision_Rz = nc.replace(vision_x, '').replace(vision_y, '').replace(vision_z, '').replace(vision_Rx, '').replace(vision_Ry, '').replace('\\', '')
    # vision_Rx = vision_Ry = vision_Rz = 0

def main_program():
    time.sleep(5)
    # stop_program()
    print "x", float(vision_x)
    print "y", float(vision_y)
    print "z", float(vision_z)
    print "Rx", float(vision_Rx)
    print "Ry", float(vision_Ry)
    print "Rz", float(vision_Rz)
    broadcaster = tf2_ros.StaticTransformBroadcaster()
    static_transformStamped = geometry_msgs.msg.TransformStamped()
    static_transformStamped.header.stamp = rospy.Time.now()
    static_transformStamped.header.frame_id = "base_link"
    static_transformStamped.child_frame_id = "landmark_location"
    static_transformStamped.transform.translation.x = float(vision_x)
    static_transformStamped.transform.translation.y = float(vision_y)
    static_transformStamped.transform.translation.z = float(vision_z)
    quat = tf.transformations.quaternion_from_euler(
               math.radians(float(vision_Rx)),math.radians(float(vision_Ry)),math.radians(float(vision_Rz)))
    static_transformStamped.transform.rotation.x = quat[0]
    static_transformStamped.transform.rotation.y = quat[1]
    static_transformStamped.transform.rotation.z = quat[2]
    static_transformStamped.transform.rotation.w = quat[3]
    broadcaster.sendTransform(static_transformStamped)
    # return nc
    return None

def handle_landmark_location(req):
    # start_program()
    #go into vision program
    time.sleep(1)
    print "entering vision program, setting DO4 to 1"
    status = client.write_coil(0004, True, unit=1)
    print(status)
    time.sleep(1)
    print "setting DO4 to 0"
    status2 = client.write_coil(0004, False, unit=1)
    print(status2)
    Thread(target = main_program).start()
    Thread(target = vision).start()
    return main_program()

if __name__ == "__main__":
    rospy.init_node('landmark_location_service_server')
    s = rospy.Service('landmark_location', TmMotion, handle_landmark_location)
    rospy.spin()
