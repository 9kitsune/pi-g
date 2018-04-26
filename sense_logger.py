##### History #####
"""
Created by Ieuan Boucher
Amended by Lok Lui

Filename: sense_logger.py
version: 7.1
Date: 20/02/2018
"""

##### Libraries #####
from sense_hat import SenseHat
from datetime import datetime
import time

##### Variable declarations #####
FILENAME = "slog"
batch_data = []
TimeZero = datetime.now()
DURATION_min = 300 #user defined monitor duration in minutes
DURATION = 60*DURATION_min #in sec


sense = SenseHat()
#event = sense.stick.get_events()
sense.clear()
blue = (0, 0, 255)
yellow = (255, 255, 0)

##### Functions #####
def file_setup(filename):
    header = ["accel_x","accel_y","accel_z"]
    header.extend(["pitch","roll","yaw","timestamp"])
    with open(filename,"w") as f:
        f.write(",".join(str(value) for value in header)+ "\n")

def log_data():
    output_string = ",".join(str(value) for value in sense_data)
    batch_data.append(output_string)

def get_sense_data():
    sense_data=[]
    
    x,y,z = [sense.get_accelerometer_raw()[key] for key in ['x','y','z']]
    sense_data.extend([x,y,z])
    
    yaw,pitch,roll = [sense.get_orientation()[key] for key in ['yaw','pitch','roll']]
    sense_data.extend([pitch,roll,yaw])

    sense_data.append(datetime.now())

    return sense_data

##### Main Program #####
if __name__ == '__main__':
    sense = SenseHat()
    batch_data= []
    sense.set_pixel = (2, 0, blue)
    CurrentTime = str(datetime.now())
    CurrentTime =''.join(CurrentTime.split())
    CurrentTime = CurrentTime[:-10]
    CurrentTime = CurrentTime[:10] + "_" +CurrentTime[10:]
    
    if FILENAME == "":
           filename = "SenseLog-"+str(CurrentTime) +".csv"
    else:
        filename = FILENAME+"-"+str(CurrentTime) +".csv"
    
    file_setup(filename)
    
    while True : 
        sense_data = get_sense_data()
        log_data()
        TIME_FROM_ZERO = (datetime.now()-TimeZero).total_seconds()  #time since logging started
        if int(TIME_FROM_ZERO) != DURATION:                           #minute has elapsed? no.
            with open(filename,"a") as f:
                for line in batch_data:
                    f.write(line + "\n")
                batch_data=[]
            time.sleep(1) #### currently 60 times per 4 seconds. time.sleep(no. of seconds)
        elif int(TIME_FROM_ZERO) == DURATION:                          #minute has elapsed? yes.
            break                                   #finish logging for csv inspection.
        for event in sense.stick.get_events():
            if event.action == "held":                # hit joystick button
                sense.show_message('stop!')
                with open(filename,"a") as f:
                    for line in batch_data:
                        f.write(line + "\n")
                    batch_data=[]
                time.sleep(1)
                sense.set_pixel = (3,0,yellow)
                exec(open('service.py').read())
            
#NUMBEROFLOGS > 0:
#NUMBEROFLOGS -= 1
#f=ma. momentum (kg ms-1) = mass * velocity
#v = u + at     #s = ut + 1/2 at^2      #s = (v+u)/2 * t        #v^2 = u^2 + 2as    #s= vt -1/2at^2



