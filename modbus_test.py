from pymodbus.client.sync import ModbusTcpClient
import struct
from ctypes import *
host = '192.168.1.2'
port = 502

client = ModbusTcpClient(host, port)
client.connect()


reg = client.read_holding_registers(7701 , 2, unit=2)
print(reg.registers)
