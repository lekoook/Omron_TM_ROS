from pymodbus.client.sync import ModbusTcpClient
import struct
import time
from ctypes import *
host = '192.168.1.2'
port = 502

client = ModbusTcpClient(host, port)
client.connect()
# address 0000 is Digital Output 0
# address 0001 is Digital Output 1
status = client.write_coil(0002, True, unit=1)
print(status)
i = 1
while i == 1:

    status = client.write_coil(0000, True, unit=1)
    time.sleep(1)
    status = client.write_coil(0000, False, unit=1)
    status = client.write_coil(0001, True, unit=1)
    time.sleep(1)
    status = client.write_coil(0001, False, unit=1)
    print(status)
