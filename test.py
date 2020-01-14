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

start_program()
#go into vision program
print "entering vision program"
status = client.write_coil(0004, True, unit=1)
print(status)

def main_program():
    #wait 15 seconds for vision program to finish
    time.sleep(15)
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
    print "moving to pickup position"
    utf8len("1,PTP(CPP,{},{},{},{},{},{},50,200,0,false)".format(j1,j2+100,j3+350,j4,j5,j6-180))
    getCheckSum("TMSCT,{},1,PTP(CPP,{},{},{},{},{},{},50,200,0,false),".format(length,j1,j2+100,j3+350,j4,j5,j6-180))
    command =  "$TMSCT,{},1,PTP(CPP,{},{},{},{},{},{},50,200,0,false),*{}".format(length,j1,j2+100,j3+350,j4,j5,j6-180,cs)
    print "Running Command:", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    BUFFER_SIZE = 1024
    data = s.recv(BUFFER_SIZE)
    rcv = data.decode("utf-8")
    print rcv
    #check robot postion
    try:
        while not rospy.is_shutdown():
            X = modbus(7001)
            Y = modbus(7003)
            Z = modbus(7005)
            time.sleep(0.1)
            #stop program when robot reached target position
            if X == j1 and Y == j2+100 and Z == j3+350:
                print "reached pickup location"
                stop_program()
                break
            if X < j1+1 and X >j1-1 and Y < j2+101 and Y >j2+99 and Z < j3+351 and Z > j3-349:
                print "reached pickup locationn"
                stop_program()
                break
            print X,  Y,  Z
    except rospy.ROSInterruptException:
        pass
    start_program()
    grip()
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
    utf8len("1,PTP(CPP,{},{},{},{},{},{},50,200,0,false)".format(j1+200,j2+100,j3+450,j4,j5,j6-180))
    getCheckSum("TMSCT,{},1,PTP(CPP,{},{},{},{},{},{},50,200,0,false),".format(length,j1+200,j2+100,j3+450,j4,j5,j6-180))
    command =  "$TMSCT,{},1,PTP(CPP,{},{},{},{},{},{},50,200,0,false),*{}".format(length,j1+200,j2+100,j3+450,j4,j5,j6-180,cs)
    print "Running Command:", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    BUFFER_SIZE = 1024
    data = s.recv(BUFFER_SIZE)
    rcv = data.decode("utf-8")
    print rcv
    time.sleep(3)
    print "moving to dropoff position"
    utf8len("1,PTP(CPP,{},{},{},{},{},{},50,200,0,false)".format(j1+200,j2+100,j3+350,j4,j5,j6-180))
    getCheckSum("TMSCT,{},1,PTP(CPP,{},{},{},{},{},{},50,200,0,false),".format(length,j1+200,j2+100,j3+350,j4,j5,j6-180))
    command =  "$TMSCT,{},1,PTP(CPP,{},{},{},{},{},{},50,200,0,false),*{}".format(length,j1+200,j2+100,j3+350,j4,j5,j6-180,cs)
    print "Running Command:", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    BUFFER_SIZE = 1024
    data = s.recv(BUFFER_SIZE)
    rcv = data.decode("utf-8")
    print rcv
    #check current robot postion
    try:
        while not rospy.is_shutdown():
            X = modbus(7001)
            Y = modbus(7003)
            Z = modbus(7005)
            time.sleep(0.1)
            #stop program when robot reached target position
            if X == j1+200 and Y == j2+100 and Z == j3+350:
                print "reached dropoff location"
                stop_program()
                break
            if X < j1+201 and X >j1-199 and Y < j2+101 and Y >j2+99 and Z < j3+351 and Z > j3-349:
                print "reached dropoff locationn"
                stop_program()
                break
            print X,  Y,  Z
    except rospy.ROSInterruptException:
        pass
    start_program()
    release()
    stop_program()

if __name__ == "__main__":
    Thread(target = main_program).start()
    Thread(target = vision).start()
