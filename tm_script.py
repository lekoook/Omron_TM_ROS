#!/usr/bin/env python3
import socket
import threading
import time
import re
import sys


def socketconnect():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    print"socket timeout:" , s.gettimeout(),"s"

def check_server():
    TCP_IP = '192.168.1.2'
    TCP_PORT = 5890
    try:
        s.connect((TCP_IP, TCP_PORT))
        print("Connected")

    except socket.error:
        print("Connection  failed")

def command():
    BUFFER_SIZE = 1024
    # command = input("Enter Command: ")
    # command = "$TMSTA,21,1,Robot[0].CoordRobot,*20"
    # command = "$TMSCT,21,1,Robot[0].CoordRobot,*22"
    # command = "$TMSTA,22,01,Robot[0].CoordRobot,*13"
    command =  "$TMSCT,39,1,PTP(JPP,0,0,90,0,90,0,10,200,0,false),*07"
    print "Running Command:", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    data = s.recv(BUFFER_SIZE)
    rcv = data.decode("utf-8")
    print (rcv)
    # command = "$TMSCT,14,1,ScriptExit(),*67"
    # # command = "$TMSCT,37,1,float[] rtool = Robot[0].CoordRobot,*24"
    # # command =  "$TMSCT,39,1,PTP(JPP,0,0,90,0,90,0,10,200,0,false),*07"
    # print "Running Command:", command
    # command = command.encode('ascii')
    # s.send(command+b"\r\n")
    # data = s.recv(BUFFER_SIZE)
    # rcv = data.decode("utf-8")
    # print (rcv)

socketconnect()
check_server()
command()


s.close()
