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

def usage():
    return "please specify joint values <j1> <j2> <j3> <j4> <j5> <j6>"

if __name__ == "__main__":
    if len(sys.argv) == 7:
        j1 = str(sys.argv[1])
        j2 = str(sys.argv[2])
        j3 = str(sys.argv[3])
        j4 = str(sys.argv[4])
        j5 = str(sys.argv[5])
        j6 = str(sys.argv[6])
    else:
        print usage()
        sys.exit(1)
    utf8len("1,PTP(JPP,{},{},{},{},{},{},50,200,0,false)".format(j1,j2,j3,j4,j5,j6))
    getCheckSum("TMSCT,{},1,PTP(JPP,{},{},{},{},{},{},50,200,0,false),".format(length,j1,j2,j3,j4,j5,j6))
    socketconnect()
    check_server()
    command()
    s.close()
