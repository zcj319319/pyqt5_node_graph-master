#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/07/13 10:37
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : transform.py
Software: PyCharm
'''
import binascii
import ctypes
import struct

ts=bytearray(b'[')
print(binascii.hexlify(ts).decode())
temp=int(binascii.hexlify(ts),16)
print(temp)