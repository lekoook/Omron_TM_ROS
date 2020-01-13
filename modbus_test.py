from pymodbus.client.sync import ModbusTcpClient
import struct
import time
import rospy
from ctypes import *
import socket
import subprocess
import os
from threading import Thread
host = '192.168.1.2'
port = 502

client = ModbusTcpClient(host, port)
client.connect()

def socketconnect():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    print"socket timeout:" , s.gettimeout(),"s"
    print"connecting to tm robot......"

def check_server():
    # ip_address = rospy.get_param("ip_address")
    # port = rospy.get_param("port")
    ip_address = "192.168.1.2"
    port = 5890
    try:
        s.bind((ip_address, port))
        print("Connected")

    except socket.error:
        print("Connection  failed. Did you run listen node?")
        exit(0)

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

start_program()
#go into vision program
print "entering vision program"
status = client.write_coil(0004, True, unit=1)
print(status)

def func1():
    time.sleep(5)
    stop_program()

def func2():
    #read tm landmark postion values
    nc = subprocess.check_output(["netcat", "-l", "9000"])
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


Thread(target = func1).start()
Thread(target = func2).start()
start_program()




# #read tm landmark postion values
# nc = subprocess.check_output(["netcat", "-l", "9000"])
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
