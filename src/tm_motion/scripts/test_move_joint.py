#!/usr/bin/env python
import socket
import threading
import time
import re
import sys
import struct

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
    print (rcv)

j1 = 0
j2 = -50
j3 = -50
j4 = -100
j5 = 50
j6 = -20
print utf8len("1,PTP(JPP,{},{},{},{},{},{},50,200,0,false)".format(j1,j2,j3,j4,j5,j6))
print getCheckSum("TMSCT,{},1,PTP(JPP,{},{},{},{},{},{},50,200,0,false),".format(length,j1,j2,j3,j4,j5,j6))
socketconnect()
check_server()
command()


s.close()
