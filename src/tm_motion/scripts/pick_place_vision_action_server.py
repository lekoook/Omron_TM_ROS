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
            "pick_place_vision", ActionAction, execute_cb=self.execute_cb, auto_start=False)
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

        def command():
            #start program
            print "starting program"
            status = client.write_coil(7104, True, unit=1)
            print(status)
            time.sleep(5)
            #go into vision program
            print "entering vision program"
            status = client.write_coil(0004, True, unit=1)
            print(status)
            time.sleep(20)
            print "griping object"
            status = client.write_coil(0000, True, unit=1)
            time.sleep(2)

            #stop program
            print "stopping program"
            status = client.write_coil(7105, True, unit=1)
            print(status)
            time.sleep(2)

            #start program
            print "starting program"
            status = client.write_coil(7104, True, unit=1)
            print(status)
            time.sleep(5)
            #go into listen node
            print "going into listen node"
            status = client.write_coil(0003, True, unit=1)
            print(status)
            time.sleep(3)
            socketconnect()
            check_server()
            print "moving to dropoff on top position"
            utf8len("1,PTP(CPP,{},{},{},{},{},{},50,200,0,false)".format(j1,j2,j3+50,j4,j5,j6))
            getCheckSum("TMSCT,{},1,PTP(CPP,{},{},{},{},{},{},50,200,0,false),".format(length,j1,j2,j3+50,j4,j5,j6))
            command =  "$TMSCT,{},1,PTP(CPP,{},{},{},{},{},{},50,200,0,false),*{}".format(length,j1,j2,j3+50,j4,j5,j6,cs)
            # command = "$TMSCT,69,1,PTP(CPP,-519.88,-202.10,280,179.47,-0.47,-89.75,100,200,0,false),*0a"
            print "Running Command:", command
            command = command.encode('ascii')
            s.send(command+b"\r\n")
            data = s.recv(BUFFER_SIZE)
            rcv = data.decode("utf-8")
            print rcv
            time.sleep(3)
            print "moving to dropoff position"
            # command = "$TMSCT,66,1,PTP(CPP,596.30,551.41,329.92,177.24,-0.58,168.35,50,200,0,false),*20"
            utf8len("1,PTP(CPP,{},{},{},{},{},{},50,200,0,false)".format(j1,j2,j3,j4,j5,j6))
            getCheckSum("TMSCT,{},1,PTP(CPP,{},{},{},{},{},{},50,200,0,false),".format(length,j1,j2,j3,j4,j5,j6))
            command =  "$TMSCT,{},1,PTP(CPP,{},{},{},{},{},{},50,200,0,false),*{}".format(length,j1,j2,j3,j4,j5,j6,cs)
            s.send(command+b"\r\n")
            BUFFER_SIZE = 1024
            data = s.recv(BUFFER_SIZE)
            rcv = data.decode("utf-8")
            print (rcv)
            time.sleep(10)
            #stop program
            print "stopping program"
            status = client.write_coil(7105, True, unit=1)
            print(status)
            time.sleep(2)

            #start program
            print "starting program"
            status = client.write_coil(7104, True, unit=1)
            print(status)
            time.sleep(5)
            #go into gipper function
            status = client.write_coil(0002, True, unit=1)
            print(status)
            time.sleep(1)
            #open gripper
            print "opening gripper"
            status = client.write_coil(0001, True, unit=1)
            time.sleep(0.5)
            #stop program
            print "stopping program"
            status = client.write_coil(7105, True, unit=1)
            print(status)

            result.status = "COMPLETED"
            print "COMPLETED"
            self.a_server.set_succeeded(result)
            return(0)

        # utf8len("1,PTP(CPP,{},{},{},{},{},{},50,200,0,false)".format(j1,j2,j3,j4,j5,j6))
        # getCheckSum("TMSCT,{},1,PTP(CPP,{},{},{},{},{},{},50,200,0,false),".format(length,j1,j2,j3,j4,j5,j6))
        # socketconnect()
        # check_server()
        command()
        s.close()


if __name__ == "__main__":
    rospy.init_node("pick_place_vision_action_server")
    s = ActionServer()
    rospy.spin()
