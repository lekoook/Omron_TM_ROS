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
po = 502

client = ModbusTcpClient(host, po)
client.connect()

class ActionServer():

    def __init__(self):
        self.a_server = actionlib.SimpleActionServer(
            "move_joint", ActionAction, execute_cb=self.execute_cb, auto_start=False)
        self.a_server.start()

    def execute_cb(self, goal):
        success = True
        feedback = ActionFeedback()
        result = ActionResult()
        function = goal.goal_function
        param = goal.goal_param
        j1 = goal.goal_goal1
        j2 = goal.goal_goal2
        j3 = goal.goal_goal3
        j4 = goal.goal_goal4
        j5 = goal.goal_goal5
        j6 = goal.goal_goal6
        def socketconnect():
            global s
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            print"socket timeout:" , s.gettimeout(),"s"
            print"connecting to tm robot......"

        def check_server():
            ip_address = rospy.get_param("ip_address")
            # port = rospy.get_param("port")
            # ip_address = '192.168.1.2'
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
        # cs = "09"
        # length = "37"
        def command():
            #go into listen node
            status = client.write_coil(0003, True, unit=1)
            print(status)
            time.sleep(1)
            BUFFER_SIZE = 1024
            command =  "$TMSCT,{},1,{}({},{},{},{},{},{},{},50,200,0,false),*{}".format(length,function,param,j1,j2,j3,j4,j5,j6,cs)
            print "Running Command:", command
            command = command.encode('ascii')
            s.send(command+b"\r\n")
            data = s.recv(BUFFER_SIZE)
            rcv = data.decode("utf-8")
            result.status = rcv
            print (rcv)

            time.sleep(10)
            #stop program
            status = client.write_coil(7105, True, unit=1)
            print(status)
            time.sleep(2)
            #start program
            status = client.write_coil(7104, True, unit=1)
            print(status)
            time.sleep(5)

            #gripper
            print "openning griper"
            status = client.write_coil(0003, False, unit=1)
            print(status)
            status = client.write_coil(0002, True, unit=1)
            print(status)
            time.sleep(1)
            status = client.write_coil(0000, True, unit=1)
            time.sleep(1)
            status = client.write_coil(0000, False, unit=1)
            # status = client.write_coil(0001, True, unit=1)
            # time.sleep(1)
            # status = client.write_coil(0001, False, unit=1)
            # print(status)
            #stop program
            print "stopping program"
            status = client.write_coil(7105, True, unit=1)
            print(status)
            time.sleep(2)
            #start program
            status = client.write_coil(7104, True, unit=1)
            print(status)
            time.sleep(5)
            #go into listen node
            print "going into listen node"
            status = client.write_coil(0003, True, unit=1)
            print(status)
            time.sleep(3)
            BUFFER_SIZE = 1024
            command = "$TMSCT,52,1,PTP(JPP,-8,-726,477,178,1.69,-0.69,50,200,0,false),*23"
            print "Running Command:", command
            command = command.encode('ascii')
            socketconnect()
            check_server()
            s.send(command+b"\r\n")
            time.sleep(5)
            data = s.recv(BUFFER_SIZE)
            rcv = data.decode("utf-8")
            result.status = rcv
            print (rcv)
            command = "$TMSCT,47,1,PTP(JPP,-125,20,57,12,93,-215,50,200,0,false),*03"
            s.send(command+b"\r\n")
            data = s.recv(BUFFER_SIZE)
            rcv = data.decode("utf-8")
            result.status = rcv
            print (rcv)
            print "COMPLETED"
            self.a_server.set_succeeded(result)
            return(0)



        utf8len("1,{}({},{},{},{},{},{},{},50,200,0,false)".format(function,param,j1,j2,j3,j4,j5,j6))
        getCheckSum("TMSCT,{},1,{}({},{},{},{},{},{},{},50,200,0,false),".format(length,function,param,j1,j2,j3,j4,j5,j6))
        socketconnect()
        check_server()
        command()
        s.close()


if __name__ == "__main__":
    rospy.init_node("move_joint_action_server")
    s = ActionServer()
    rospy.spin()
