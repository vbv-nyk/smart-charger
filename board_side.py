import machine
import time

def charge_or_not(charge,status,response):
    relay_pin = machine.Pin(5, machine.Pin.OUT)
    relay_pin.value(0)
    while response==1:
        if charge<=60 and status == False:
            relay_pin.value(1)
        elif charge==95 and status==True:
            relay_pin.value(0)
        
    