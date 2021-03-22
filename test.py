from PyMCP2221A import SMBus

import time

bus = SMBus.SMBus()

# Release RTC 3231


# Setup RTC 3231 for temperature reading

address = 0x68
CONV = 32

w  = ["SUN","Mon","Tues","Wed","Thur","Fri","Sat"];

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

def ReadTime(address):
    sec = bus.read_byte_data(0x68, 0)
    min = bus.read_byte_data(0x68, 1)
    hour = bus.read_byte_data(0x68, 2)
    day = bus.read_byte_data(0x68, 3)
    date = bus.read_byte_data(0x68, 4)
    month = bus.read_byte_data(0x68, 5)
    year = bus.read_byte_data(0x68, 6)
    return (hour,min,sec,date,month,year, day)

def SetTime(address):
    bus.write_byte_data(0x68, 0x00, 0x00) # set seconds and start clock
    bus.write_byte_data(0x68, 0x01, 0x38) # set minutes
    bus.write_byte_data(0x68, 0x02, 0x13) # set hours in 24 hour mode
    bus.write_byte_data(0x68, 0x03, 0x04) # set day of week
    bus.write_byte_data(0x68, 0x04, 0x07) # set date
    bus.write_byte_data(0x68, 0x05, 0x03) # set month
    bus.write_byte_data(0x68, 0x06, 0x15) # set year - last 2 digits
    
SetTime(address)
while True:
    t=ReadTime(address)
    hour1=t[0]&0x3F
    min1=t[1]&0x7F
    sec1=t[2]&0x7F
    date1=t[3]
    month1=t[4]&0x1F
    year1=t[5]
    day1=t[6]&0x3F
    print(t)
    print("%s/%s/%s %s:%s:%s %s" %(date1,month1,year1,hour1,min1,sec1,w[day1-1]))

    '''Celsius = getTemp(address)
    Fahrenheit = 9.0/5.0 * Celsius + 32
    print (Fahrenheit, "*F /", Celsius, "*C")'''
    time.sleep(1)
