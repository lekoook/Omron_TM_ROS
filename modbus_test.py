from pymodbus.client.sync import ModbusTcpClient
import struct
from ctypes import *
host = '192.168.1.2'
port = 502

client = ModbusTcpClient(host, port)
client.connect()
#
# address = 7701
# reg = client.read_input_registers(address,98,unit=1)
# print(reg.registers)

# First digital input address
address = 7701
# Written value

# It will send '11111111' to the output
client.write_registers(7701, 1161011151161169248)
