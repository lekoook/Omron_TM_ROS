from pymodbus.client.sync import ModbusTcpClient
import struct
from ctypes import *
host = '192.168.1.2'
port = 502

client = ModbusTcpClient(host, port)
client.connect()

rr = client.read_coils(7208,2,unit=2)
print rr.bits[0]
# rr = client.read_input_registers(7208,1,unit=2)
# a = rr.registers
# b = rr.registers[1]
# print a
# if rr.registers[1]<10000:
#     if rr.registers[0]<1000:
#         a = '{:04x}'.format(rr.registers[0])
#         b = '{:04x}'.format(rr.registers[1])
#         c = a+b
#         value = "%.2f" % struct.unpack('!f', c.decode('hex'))[0]
#         print value
#     else:
#         a = hex(rr.registers[0])[2:]
#         b = '{:04x}'.format(rr.registers[1])
#         c = a+b
#         # print c
#         value = "%.2f" % struct.unpack('!f', c.decode('hex'))[0]
#         print value
# else:
#     a = hex(rr.registers[0])[2:]
#     b = hex(rr.registers[1])[2:]
#     c = a+b
#     # print c
#     value = "%.2f" % struct.unpack('!f', c.decode('hex'))[0]
#     print value
