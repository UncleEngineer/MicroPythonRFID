from machine import UART
import time
from pyb import LED

uart = UART(3,9600) # uart 3 of pyd
uart.init(9600,bits=8,parity=None,stop=1)
count = 0
led1 = LED(1)
led2 = LED(2)

user = ['300047939A7E','0D001289F365']

while True:
    
    print('COUNT',count)
    try:
        data = str(uart.read().decode('utf-8'))
        ID = data.replace('\x02','').split('\x03')[0]
    except:
        data = str(uart.read())
        ID = None
    # print('Found:',[data])
    print('ID:',ID)
    if ID != None:
        if ID == '300047939A7E':
            print('USER 1')
            led1.toggle()
            led1.on()
            time.sleep(1)
            led1.off()
            time.sleep(1)
        elif ID == '0D001289F365':
            print('USER 2')
            led2.toggle()
            led2.on()
            time.sleep(1)
            led2.off()
            time.sleep(1)
        else:
            print('Not found')
            time.sleep(1)
    else:
        count += 1
        time.sleep(1)
