#!/usr/bin/env python
import socket
import threading
import time
import re
import sys
import struct
import rospy
import actionlib
from std_msgs.msg import String
from tm_motion.msg import ActionAction, ActionFeedback, ActionResult
from pymodbus.client.sync import ModbusTcpClient
import struct
import time
from ctypes import *
host = '192.168.1.2'
port_modbus = 502

client = ModbusTcpClient(host, port_modbus)
client.connect()

class ActionServer():

    def __init__(self):
        self.a_server = actionlib.SimpleActionServer(
            "move_action", ActionAction, execute_cb=self.execute_cb, auto_start=False)
        self.a_server.start()

    def execute_cb(self, goal):
        success = True
        feedback = ActionFeedback()
        result = ActionResult()
        function = goal.goal_function
        param = goal.goal_param
        j1 = float(goal.goal_goal1)
        j2 = float(goal.goal_goal2)
        j3 = float(goal.goal_goal3)
        j4 = float(goal.goal_goal4)
        j5 = float(goal.goal_goal5)
        j6 = float(goal.goal_goal6)
        def socketconnect():
            global s
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            print"socket timeout:" , s.gettimeout(),"s"
            print"connecting to tm robot......"

        def check_server():
            # ip_address = rospy.get_param("ip_address")
            # port = rospy.get_param("port")
            ip_address = '192.168.1.2'
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

        def command():
            start_program()
            #go into listen node
            print "going into listen node"
            status = client.write_coil(0003, True, unit=1)
            print(status)
            time.sleep(2)
            socketconnect()
            check_server()
            print "moving to pickup position"
            utf8len("1,PTP(CPP,{},{},{},{},{},{},50,200,0,false)".format(j1,j2,j3,j4,j5,j6))
            getCheckSum("TMSCT,{},1,PTP(CPP,{},{},{},{},{},{},50,200,0,false),".format(length,j1,j2,j3,j4,j5,j6))
            command =  "$TMSCT,{},1,PTP(CPP,{},{},{},{},{},{},50,200,0,false),*{}".format(length,j1,j2,j3,j4,j5,j6,cs)
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
                        stop_program()
                        result.status = "Moved to location"
                        print "Moved to location"
                        self.a_server.set_succeeded(result)
                        return(0)
                    if X < j1+1 and X >j1-1 and Y < j2+101 and Y >j2+99 and Z < j3+351 and Z > j3-349:
                        stop_program()
                        result.status = "Moved to location"
                        print "Moved to location"
                        self.a_server.set_succeeded(result)
                        return(0)
                    print X,  Y,  Z
            except rospy.ROSInterruptException:
                pass

        command()

if __name__ == "__main__":
    rospy.init_node("move_action_server")
    s = ActionServer()
    rospy.spin()
