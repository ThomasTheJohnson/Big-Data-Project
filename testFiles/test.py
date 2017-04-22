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

temperature1 = sense.get_temperature_from_humidity()
temperature2 = sense.get_temperature_from_pressure()
machineTemp = cpuTemp()

temp = (temperature1+temperature2)/2
accountForCPU = temp - ((machineTemp - temp)/1.5)
temp = c_to_f(accountForCPU)

pressure = sense.get_pressure()
humidity = sense.get_humidity()

print "- Temperatures in Farenheit - "
print "Current CPU Temperature: %d" % (c_to_f(machineTemp))
print "Current Average Temperature from Sensors: %d" % (c_to_f((temperature1+temperature2)/2))
print "Ambient Temperature Accounting for CPU Heat: %d" % (temp)
print "#" * 20
print "- Cycling Display - "
print "Displaying Orange Arrow"
displayRise(sense)
time.sleep(5)
print "Displaying Blue Arrow"
displayDrop(sense)
time.sleep(5)
print "Displaying Sun"
displaySun(sense)
time.sleep(5)
print "Displaying Rain"
displayRain(sense)
time.sleep(5)
off(sense)
print "Display Test Complete"
print "#" * 20
