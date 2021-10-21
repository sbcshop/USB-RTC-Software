#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyMCP2221A import SMBus

import time
 
address = 0x68  #i2c address of DS3231
register = 0x00
CONV = 32

w  = ["SUN","Mon","Tues","Wed","Thur","Fri","Sat"];

#/dev/i2c-1
bus = SMBus.SMBus()
def ds3231SetTime():
    #bus.write_i2c_block_data(address,register,NowTime)
    bus.write_byte_data(0x68, 0x00, NowTime[0]) # set seconds and start clock
    bus.write_byte_data(0x68, 0x01, NowTime[1]) # set minutes
    bus.write_byte_data(0x68, 0x02, NowTime[2]) # set hours in 24 hour mode
    bus.write_byte_data(0x68, 0x03, NowTime[3]) # set day of week
    bus.write_byte_data(0x68, 0x04, NowTime[4]) # set date
    bus.write_byte_data(0x68, 0x05, NowTime[5]) # set month
    bus.write_byte_data(0x68, 0x06, NowTime[6]) # set year - last 2 digits
 
def ds3231ReadTime():
    return bus.read_i2c_block_data(address,register,7);

# Force a conversion and wait until it completes
def convTemp(address):
    byte_control = bus.read_byte_data(address,0x0E)
    if byte_control&CONV == 0:
        bus.write_byte_data(address, 0x0E, byte_control|CONV)
    byte_control = bus.read_byte_data(address,0x0E)
    while byte_control&CONV != 0:
        #time.sleep(1)
        byte_control = bus.read_byte_data(address,0x0E)
    return True

# Get temperature in degrees C
def getTemp(address):
    convTemp(address)
    byte_tmsb = bus.read_byte_data(address,0x11)
    byte_tlsb = bus.read_byte_data(address,0x12)
    tinteger = (byte_tmsb & 0x7f) + ((byte_tmsb & 0x80) >> 7) * -2**8
    tdecimal = (byte_tmsb >> 7) * 2**(-1) + ((byte_tmsb & 0x40) >> 6) * 2**(-2)
    return tinteger + tdecimal
 
while 1:
    t = ds3231ReadTime()
    t[0] = t[0]&0x7F  #sec
    t[1] = t[1]&0x7F  #min
    t[2] = t[2]&0x3F  #hour
    t[3] = t[3]&0x07  #week
    t[4] = t[4]&0x3F  #day
    t[5] = t[5]&0x1F  #month
    print("20%x/%x/%x %x:%x:%x  %s" %(t[6],t[5],t[4],t[2],t[1],t[0],w[t[3]-1]))
    time.sleep(1)

    '''Celsius = getTemp(address)
    Fahrenheit = 9.0/5.0 * Celsius + 32
    print (Fahrenheit, "*F /", Celsius, "*C")
    time.sleep(1)'''
