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

class ActionServer():
    action_command = None
    def move_joint(self,result,feedback):

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
            BUFFER_SIZE = 1024
            command =  "$TMSCT,{},1,PTP(JPP,{},{},{},{},{},{},50,200,0,false),*{}".format(length,j1,j2,j3,j4,j5,j6,cs)
            print "Running Command:", command
            command = command.encode('ascii')
            s.send(command+b"\r\n")
            data = s.recv(BUFFER_SIZE)
            rcv = data.decode("utf-8")
            result.status = rcv
            print (rcv)
            self.a_server.set_succeeded(result)
            return(0)

        utf8len("1,PTP(JPP,{},{},{},{},{},{},50,200,0,false)".format(j1,j2,j3,j4,j5,j6))
        getCheckSum("TMSCT,{},1,PTP(JPP,{},{},{},{},{},{},50,200,0,false),".format(length,j1,j2,j3,j4,j5,j6))
        socketconnect()
        check_server()
        command()
        s.close()

def usage():
    return "please specify joint values and ip address <ip_address> <j1> <j2> <j3> <j4> <j5> <j6>"

def __init__(self, action_name):
        self.action_command = action_name
        self.a_server = actionlib.SimpleActionServer(
            action_name, ActionAction, execute_cb=self.execute_cb, auto_start=False)
        self.a_server.start()

def execute_cb(self, goal):
        success = True
        feedback = ActionFeedback()
        result = ActionResult()
        joint_values = goal.goal_goal

        if self.action_command == "move_joint":
            self.move_joint(result, feedback)

if __name__ == "__main__":
    rospy.init_node("move_joint_action_server")
    s = ActionServer("move_joint")
    rospy.spin()
