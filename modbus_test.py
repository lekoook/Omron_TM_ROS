from pymodbus.client.sync import ModbusTcpClient
import struct
import bitstring
from ctypes import *
host = '192.168.1.2'
port = 502

client = ModbusTcpClient(host, port)
client.connect()


rr = client.read_input_registers(7001,2,unit=2)
a = rr.registers[0]
b = rr.registers[1]
print a, b
