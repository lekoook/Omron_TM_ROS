from pymodbus.client.sync import ModbusTcpClient
import struct
import time
import rospy
from ctypes import *
import socket
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
    ip_address = '192.168.1.2'
    port = 5890
    try:
        s.connect((ip_address, port))
        print("Connected")

    except socket.error:
        print("Connection  failed. Did you run listen node?")
        exit(0)

#start program
print "starting program"
status = client.write_coil(7104, True, unit=1)
print(status)
time.sleep(5)
#go into vision program
status = client.write_coil(0004, True, unit=1)
print(status)
time.sleep(15)
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
command = "$TMSCT,66,1,PTP(CPP,596.30,551.41,329.92,177.24,-0.58,168.35,50,200,0,false),*20"
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
exit(0)
