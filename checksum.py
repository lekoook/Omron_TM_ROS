#!/usr/bin/env python3
import socket
import threading
import time
import re
import sys

def getCheckSum(sentence):
    calc_cksum = 0
    for s in sentence:
        calc_cksum ^= ord(s)
    return str(hex(calc_cksum)).lstrip("0").lstrip("x")

print getCheckSum("TMSCT,37,1,PTP(JPP,0,0,0,0,0,0,10,200,0,false),")

def utf8len(s):
    return len(s.encode('utf-8'))

print utf8len("1,PTP(JPP,0,0,0,0,0,0,10,200,0,false)")
