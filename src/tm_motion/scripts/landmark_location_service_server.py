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
host = '192.168.1.2'
port = 502
client = ModbusTcpClient(host, port)
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

def vision():
    global vision_x, vision_y, vision_z, vision_Rx, vision_Ry, vision_Rz
    #read tm landmark postion values
    nc = subprocess.check_output(["netcat", "-l", "9000"])
    vision_x = nc.partition("\\")[0]
    vision_y = nc.partition("\\\\")[0].replace(vision_x, '').replace('\\', '')
    vision_z = nc.partition("\\\\\\")[0].replace(vision_x, '').replace(vision_y, '').replace('\\', '')
    vision_Rx = nc.partition("\\\\\\\\")[0].replace(vision_x, '').replace(vision_y, '').replace(vision_z, '').replace('\\', '')
    vision_Ry = nc.partition("\\\\\\\\\\")[0].replace(vision_x, '').replace(vision_y, '').replace(vision_z, '').replace(vision_Rx, '').replace('\\', '')
    vision_Rz = nc.replace(vision_x, '').replace(vision_y, '').replace(vision_z, '').replace(vision_Rx, '').replace(vision_Ry, '').replace('\\', '')

def main_program():
    time.sleep(8)
    stop_program()
    print float(vision_x)
    print float(vision_y)
    print float(vision_z)
    print float(vision_Rx)
    print float(vision_Ry)
    print float(vision_Rz)

if __name__ == "__main__":
    start_program()
    #go into vision program
    print "entering vision program"
    status = client.write_coil(0004, True, unit=1)
    print(status)
    Thread(target = main_program).start()
    Thread(target = vision).start()
