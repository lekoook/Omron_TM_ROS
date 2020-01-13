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
        s.connect((ip_address, port))
        print("Connected")

    except socket.error:
        print("Connection  failed. Did you run listen node?")
        exit(0)

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
    print float(vision_x)
    print float(vision_y)
    print float(vision_z)
    print float(vision_Rx)
    print float(vision_Ry)
    print float(vision_Rz)

start_program()
#go into vision program
print "entering vision program"
status = client.write_coil(0004, True, unit=1)
print(status)

def main_program():
    time.sleep(10)
    stop_program()
    start_program()
    #go into listen node
    print "going into listen node"
    status = client.write_coil(0003, True, unit=1)
    print(status)
    time.sleep(2)
    socketconnect()
    check_server()
    j1 = float(vision_x)
    j2 = float(vision_y)
    j3 = float(vision_z)
    j4 = float(vision_Rx)
    j5 = float(vision_Ry)
    j6 = float(vision_Rz)
    print "moving to dropoff on top position"
    utf8len("1,PTP(CPP,{},{},{},{},{},{},50,200,0,false)".format(j1,j2,j3+100,j4,j5,j6))
    getCheckSum("TMSCT,{},1,PTP(CPP,{},{},{},{},{},{},50,200,0,false),".format(length,j1,j2,j3+100,j4,j5,j6))
    command =  "$TMSCT,{},1,PTP(CPP,{},{},{},{},{},{},50,200,0,false),*{}".format(length,j1,j2,j3+100,j4,j5,j6,cs)
    print "Running Command:", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    BUFFER_SIZE = 1024
    data = s.recv(BUFFER_SIZE)
    rcv = data.decode("utf-8")
    print rcv

Thread(target = main_program).start()
Thread(target = vision).start()
