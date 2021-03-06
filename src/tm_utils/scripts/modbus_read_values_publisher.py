#!/usr/bin/env python
from pymodbus.client.sync import ModbusTcpClient
import struct
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Pose
from ctypes import *
import numpy as np
# ip_address = '192.168.1.2'
# port = 502
ip_address = rospy.get_param("ip_address")
port = rospy.get_param("port")

client = ModbusTcpClient(ip_address, port)
client.connect()
def euler_to_quaternion(yaw, pitch, roll):
    global qx, qy, qz, qw
    qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
    qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
    qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
    qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)

def modbus(address):
    rr = client.read_input_registers(address,2,unit=2)
    # print rr.registers
    if rr.registers[1]<10000:
        if rr.registers[0]<1000:
            a = '{:04x}'.format(rr.registers[0])
            b = '{:04x}'.format(rr.registers[1])
            c = a+b
            value = "%.2f" % struct.unpack('!f', c.decode('hex'))[0]
            return float(value)
        else:
            a = hex(rr.registers[0])[2:]
            b = '{:04x}'.format(rr.registers[1])
            c = a+b
            value = "%.2f" % struct.unpack('!f', c.decode('hex'))[0]
            return float(value)
    else:
        a = hex(rr.registers[0])[2:]
        b = hex(rr.registers[1])[2:]
        c = a+b
        value = "%.2f" % struct.unpack('!f', c.decode('hex'))[0]
        return float(value)

def cartesian_coordinate_wrt_current_Base_without_tool():
    X = modbus(7001)
    Y = modbus(7003)
    Z = modbus(7005)
    Rx = modbus(7007)
    Ry = modbus(7009)
    Rz = modbus(7011)
    euler_to_quaternion(Rx, Ry, Rz)
    pub = rospy.Publisher('Cartesian_coordinate_wrt_current_Base_without_tool', Pose, queue_size=10)
    msg = Pose()
    msg.position.x = X
    msg.position.y = Y
    msg.position.z = Z
    msg.orientation.x = float("%.2f" %qx)
    msg.orientation.y = float("%.2f" %qy)
    msg.orientation.z = float("%.2f" %qz)
    msg.orientation.w = float("%.2f" %qw)
    rospy.loginfo(msg)
    pub.publish(msg)
    rospy.sleep(0.1)

def joint_values():
    j1 = modbus(7013)
    j2 = modbus(7015)
    j3 = modbus(7017)
    j4 = modbus(7019)
    j5 = modbus(7021)
    j6 = modbus(7023)
    pub = rospy.Publisher('joint_state', JointState, queue_size=10)
    msg = JointState()
    msg.header.stamp = rospy.Time.now()
    msg.name = ['joint 1(in degrees)', 'joint 2', 'joint 3', 'joint 4', 'joint 5', 'joint 6']
    msg.position = [j1, j2, j3, j4, j5, j6]
    msg.effort = []
    rospy.loginfo(msg)
    pub.publish(msg)
    rospy.sleep(0.1)

def cartesian_coordinate_wrt_current_Base_with_tool():
    X = modbus(7025)
    Y = modbus(7027)
    Z = modbus(7029)
    Rx = modbus(7031)
    Ry = modbus(7033)
    Rz = modbus(7035)
    euler_to_quaternion(Rx, Ry, Rz)
    pub = rospy.Publisher('Cartesian_coordinate_wrt_current_Base_with_tool', Pose, queue_size=10)
    msg = Pose()
    msg.position.x = X
    msg.position.y = Y
    msg.position.z = Z
    msg.orientation.x = float("%.2f" %qx)
    msg.orientation.y = float("%.2f" %qy)
    msg.orientation.z = float("%.2f" %qz)
    msg.orientation.w = float("%.2f" %qw)
    rospy.loginfo(msg)
    pub.publish(msg)
    rospy.sleep(0.1)


if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            rospy.init_node('modbus_read_values_publisher', anonymous=True)
            cartesian_coordinate_wrt_current_Base_without_tool()
            # rospy.sleep(1)
            joint_values()
            # rospy.sleep(1)
            cartesian_coordinate_wrt_current_Base_with_tool()
            #rospy.sleep(1)
    except rospy.ROSInterruptException:
        pass

# modbus(7001, "X (Cartesian coordinate w.r.t. current Base without tool):", "mm")
# modbus(7003, "Y (Cartesian coordinate w.r.t. current Base without tool):", "mm")
# modbus(7005, "Z (Cartesian coordinate w.r.t. current Base without tool):", "mm")
# modbus(7007, "Rx (Cartesian coordinate w.r.t. current Base without tool):", "degree")
# modbus(7009, "Ry (Cartesian coordinate w.r.t. current Base without tool):", "degree")
# modbus(7011, "Rz (Cartesian coordinate w.r.t. current Base without tool):", "degree")
# modbus(7013, "Joint 1:", "degree")
# modbus(7015, "Joint 2:", "degree")
# modbus(7017, "Joint 3:", "degree")
# modbus(7019, "Joint 4:", "degree")
# modbus(7021, "Joint 5:", "degree")
# modbus(7023, "Joint 6:", "degree")
# modbus(7025, "X (Cartesian coordinate w.r.t. current Base with tool):", "mm")
# modbus(7027, "Y (Cartesian coordinate w.r.t. current Base with tool):", "mm")
# modbus(7029, "Z (Cartesian coordinate w.r.t. current Base with tool):", "mm")
# modbus(7031, "Rx (Cartesian coordinate w.r.t. current Base with tool):", "degree")
# modbus(7033, "Ry (Cartesian coordinate w.r.t. current Base with tool):", "degree")
# modbus(7035, "Rz (Cartesian coordinate w.r.t. current Base with tool):", "degree")
