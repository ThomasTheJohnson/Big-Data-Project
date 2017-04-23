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
	senseName.load_image('img/rise1.png')

def displayDrop(senseName):
	senseName.load_image('img/drop1.png')

def off(senseName):
	senseName.clear()

################# SenseHat Objects ################################

sense = SenseHat()

################ Variables ########################################

tempList = [50,50,50,50,50]
riseOrDrop = 0
loopCount = 0
lastTemp = 0
url = 'http://52.33.110.204/node/weather/api/stationdata'
stationid = 1 #This is the unique ID for my personal station.

############### "Main" Execution ####################################

while True:
    ##Clears the display so that it is not always on.##
    off(sense)

    ##Reads the temperature from two different sensors##
    ##Also reads the temperature from the CPU##
    temperature1 = sense.get_temperature_from_humidity()
    temperature2 = sense.get_temperature_from_pressure()
    machineTemp = cpuTemp()

    ##Takes the average of the sensor reads##
    ##Accounts for the CPU temperature##
    ##Converts to Farenheit because I don't get Celsius##
    temp = (temperature1+temperature2)/2
    accountForCPU = temp - ((machineTemp - temp)/1.5)
    temp = c_to_f(accountForCPU)

    ##Adds the current temperature read to a list of 5 temperatures##
    ##Removes the oldest temperature in memory##
    tempList.append(temp)
    tempList.pop(0)

    ##Checks to see how many times the program has looped##
    loopCount = loopCount % 5

    ##If it is the fifth time the program has looped then we enter##
    if(loopCount == 0):
        ##Takes the average of the last 5 temperature reads##
	    avgTemp = 0
        for nums in tempList:
            avgTemp += nums
        avgTemp = avgTemp/len(tempList)

        ##Subtracts the current average of the 5 reads with the previous##
        riseOrDrop = lastTemp - avgTemp
        lastTemp = avgTemp

        ##If riseOrDrop is positive I.E. the previous average was greater than then current##
        ##the LED matrix displays a drop in temperature or vice versa##
        if(riseOrDrop > 0):
            displayDrop(sense)
        else:
            displayRise(sense)

    ##Reads the pressure and humidity sensors##
    pressure = sense.get_pressure()*.02953 #In Hg
    humidity = sense.get_humidity() #In %rH

    ##Creates a HTTP Post payload with data##
    payload = {
        'station_id': stationid,
        'temperature': temp,
        'humidity': humidity,
        'pressure': pressure
    }

    ##Posts the data to our web server.
    r = requests.post(url, data=payload)
    loopCount += 1
    ##Waits 10 seconds before reading again##
    time.sleep(10)
