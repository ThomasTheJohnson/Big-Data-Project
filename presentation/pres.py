from sense_hat import SenseHat
import time
import os
import datetime
import requests

################## Functions #######################################

def c_to_f(input):
    return (input*9/5)+32

def cpuTemp():
    reading = os.popen("vcgencmd measure_temp").readline()
    temp = float(reading.replace("temp=","").replace("'C\n",""))
    return(temp)

################# Display Functions ###############################

def displayRise(senseName):
	senseName.load_image('testImg/rise1.png')

def displayDrop(senseName):
	senseName.load_image('testImg/drop1.png')

def displayRain(senseName):
    senseName.load_image('testImg/rain1.png')

def displaySun(senseName):
    senseName.load_image('testImg/sun1.png')

def off(senseName):
	senseName.clear()

################# SenseHat Objects ################################

sense = SenseHat()

############### "Main" Execution ####################################

while True:
    displayRise(sense)
    time.sleep(5)

    displayDrop(sense)
    time.sleep(5)

    displaySun(sense)
    time.sleep(5)

    displayRain(sense)
    time.sleep(5)
