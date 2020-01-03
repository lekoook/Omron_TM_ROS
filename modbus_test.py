from pymodbus.client.sync import ModbusTcpClient
import struct
import time
from ctypes import *
host = '192.168.1.2'
port = 502

client = ModbusTcpClient(host, port)
client.connect()


# reg = client.read_holding_registers(7701 , 2, unit=2)
# print(reg.registers)
# status = client.write_coil(0001, True, unit=1)
i = 1
while i == 1:

    status = client.write_coil(0000, True, unit=1)
    time.sleep(1)
    status = client.write_coil(0000, False, unit=1)
    status = client.write_coil(0001, True, unit=1)
    time.sleep(1)
    status = client.write_coil(0001, False, unit=1)
    print(status)
