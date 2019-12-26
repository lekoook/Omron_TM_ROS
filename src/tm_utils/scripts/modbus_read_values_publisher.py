#!/usr/bin/env python
from pymodbus.client.sync import ModbusTcpClient
import struct
import rospy
from std_msgs.msg import String
from ctypes import *
# ip_address = '192.168.1.2'
# port = 502
ip_address = rospy.get_param("ip_address")
port = rospy.get_param("port")

client = ModbusTcpClient(ip_address, port)
client.connect()
rospy.init_node('modbus_read_values_publisher', anonymous=True)
def modbus(address, data, units, topic_name):
    pub = rospy.Publisher(topic_name, String, queue_size=10)
    rr = client.read_input_registers(address,2,unit=2)
    # print rr.registers
    if rr.registers[1]<10000:
        if rr.registers[0]<1000:
            a = '{:04x}'.format(rr.registers[0])
            b = '{:04x}'.format(rr.registers[1])
            c = a+b
            value = data, "%.2f" % struct.unpack('!f', c.decode('hex'))[0], units
            print value
            pub.publish(str(value))
        else:
            a = hex(rr.registers[0])[2:]
            b = '{:04x}'.format(rr.registers[1])
            c = a+b
            # print c
            value = data, "%.2f" % struct.unpack('!f', c.decode('hex'))[0], units
            print value
            pub.publish(str(value))
    else:
        a = hex(rr.registers[0])[2:]
        b = hex(rr.registers[1])[2:]
        c = a+b
        # print c
        value = data, "%.2f" % struct.unpack('!f', c.decode('hex'))[0], units
        print value
        pub.publish(str(value))
    rospy.sleep(0.1)

if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            modbus(7001, "X (Cartesian coordinate w.r.t. current Base without tool):", "mm", "X_currentBase_woTool")
            modbus(7003, "Y (Cartesian coordinate w.r.t. current Base without tool):", "mm", "Y_currentBase_woTool")
            modbus(7005, "Z (Cartesian coordinate w.r.t. current Base without tool):", "mm", "Z_currentBase_woTool")
            modbus(7007, "Rx (Cartesian coordinate w.r.t. current Base without tool):", "degree", "Rx_currentBase_woTool")
            modbus(7009, "Ry (Cartesian coordinate w.r.t. current Base without tool):", "degree", "Ry_currentBase_woTool")
            modbus(7011, "Rz (Cartesian coordinate w.r.t. current Base without tool):", "degree", "Rz_currentBase_woTool")
            modbus(7013, "Joint 1:", "degree", "Joint1")
            modbus(7015, "Joint 2:", "degree", "Joint2")
            modbus(7017, "Joint 3:", "degree", "Joint3")
            modbus(7019, "Joint 4:", "degree", "Joint4")
            modbus(7021, "Joint 5:", "degree", "Joint5")
            modbus(7023, "Joint 6:", "degree", "Joint6")
            modbus(7025, "X (Cartesian coordinate w.r.t. current Base with tool):", "mm", "X_currentBase_wTool")
            modbus(7027, "Y (Cartesian coordinate w.r.t. current Base with tool):", "mm", "Y_currentBase_wTool")
            modbus(7029, "Z (Cartesian coordinate w.r.t. current Base with tool):", "mm", "Z_currentBase_wTool")
            modbus(7031, "Rx (Cartesian coordinate w.r.t. current Base with tool):", "degree", "Rx_currentBase_wTool")
            modbus(7033, "Ry (Cartesian coordinate w.r.t. current Base with tool):", "degree", "Ry_currentBase_wTool")
            modbus(7035, "Rz (Cartesian coordinate w.r.t. current Base with tool):", "degree", "Rz_currentBase_wTool")
    except rospy.ROSInterruptException:
        pass

# modbus(7001, "X (Cartesian coordinate w.r.t. current Base without tool):", "mm")
# modbus(7003, "Y (Cartesian coordinate w.r.t. current Base without tool):", "mm")
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
