# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 16:15:42 2018

@author: k0olu
"""
"""
auto start up service to initiate logger
and a place for the logger to exit back to, to start logger again.
"""

from sense_hat import SenseHat
from time import sleep


sense = SenseHat()
green = (0, 255, 0)
red = (255, 0, 0)
    
    
#def held(event):
#    print('exiting')
#    sense.show_message('bye')
#    sleep(1)
#    exit()
    

if __name__ == '__main__':
    sense.clear()
    print('Ready')
    sleep(1)
    sense.set_pixel(0, 0, green)
    
# tell the program which function is associate to which joystick action.
#sense.stick.direction_middle = pressed
#    sense.stick.direction_middle = pressed
#    sense.stick.direction_down = held
while True:
    for event in sense.stick.get_events():
        if (event.direction == "middle"):
            print('start logging')
            sense.show_message('start logging')
            exec(open('sense_logger.py').read())
    
        if (event.direction == "down"):
            print('script end')
            sense.show_message('bye...', text_colour=red)
            sleep(1)
            exit()

#this keeps the program running to receive joystick action