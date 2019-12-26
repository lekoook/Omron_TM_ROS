#!/usr/bin/env python
from pymodbus.client.sync import ModbusTcpClient
import struct
import rospy
from std_msgs.msg import String
from ctypes import *
# host = '192.168.1.2'
# port = 502
ip_address = rospy.get_param("ip_address")
port = rospy.get_param("port")

client = ModbusTcpClient(ip_address, port)
client.connect()
rospy.init_node('modbus_read_values_publisher', anonymous=True)
def modbus(address, data, units):
    rr = client.read_input_registers(address,2,unit=2)
    # print rr.registers
    if rr.registers[1]<10000:
        if rr.registers[0]<1000:
            a = '{:04x}'.format(rr.registers[0])
            b = '{:04x}'.format(rr.registers[1])
            c = a+b
            return data, "%.2f" % struct.unpack('!f', c.decode('hex'))[0], units
        else:
            a = hex(rr.registers[0])[2:]
            b = '{:04x}'.format(rr.registers[1])
            c = a+b
            # print c
            return data, "%.2f" % struct.unpack('!f', c.decode('hex'))[0], units
    else:
        a = hex(rr.registers[0])[2:]
        b = hex(rr.registers[1])[2:]
        c = a+b
        # print c
        return data, "%.2f" % struct.unpack('!f', c.decode('hex'))[0], units

def X_cbwot():
    pub = rospy.Publisher('X_currentBase_woTool', String, queue_size=10)
    print modbus(7001, "X (Cartesian coordinate w.r.t. current Base without tool):", "mm")
    pub.publish(str(modbus(7001, "X (Cartesian coordinate w.r.t. current Base without tool):", "mm")))
    rospy.sleep(1.)

def Y_cbwot():
    pub = rospy.Publisher('Y_currentBase_woTool', String, queue_size=10)
    print modbus(7003, "Y (Cartesian coordinate w.r.t. current Base without tool):", "mm")
    pub.publish(str(modbus(7003, "Y (Cartesian coordinate w.r.t. current Base without tool):", "mm")))
    rospy.sleep(1.)

if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            X_cbwot()
            Y_cbwot()


    except rospy.ROSInterruptException:
        pass

# modbus(7005, "Z (Cartesian coordinate w.r.t. current Base without tool):", "mm")
# modbus(7007, "Rx (Cartesian coordinate w.r.t. current Base without tool):", "degree")
# modbus(7009, "Ry (Cartesian coordinate w.r.t. current Base without tool):", "degree")
# modbus(7011, "Rz (Cartesian coordinate w.r.t. current Base without tool):", "degree")
# modbus(7013, "Joint 1:", "degree")
# modbus(7015, "Joint 2:", "degree")
# modbus(7017, "Joint 3:", "degree")
# modbus(7019, "Joint 4:", "degree")
# modbus(7021, "Joint 5:", "degree")
# modbus(7023, "Joint 6:", "degree")
# modbus(7025, "X (Cartesian coordinate w.r.t. current Base with tool):", "mm")
# modbus(7027, "Y (Cartesian coordinate w.r.t. current Base with tool):", "mm")
# modbus(7029, "Z (Cartesian coordinate w.r.t. current Base with tool):", "mm")
# modbus(7031, "Rx (Cartesian coordinate w.r.t. current Base with tool):", "degree")
# modbus(7033, "Ry (Cartesian coordinate w.r.t. current Base with tool):", "degree")
# modbus(7035, "Rz (Cartesian coordinate w.r.t. current Base with tool):", "degree")
