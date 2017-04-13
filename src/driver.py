from sense_hat import SenseHat
import display
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

################# SenseHat Objects ################################
sense = SenseHat()
sense.set_rotation(180)


################ Variables ########################################
tempList = [50,50,50,50,50]
riseOrDrop = 0
loopCount = 0
lastTemp = 0
url = 'http://52.33.110.204/node/weather/api/stationdata'
stationid = 1

############### "Main" Execution ####################################
while True:

    display.off(sense)

    temperature1 = sense.get_temperature_from_humidity()
    temperature2 = sense.get_temperature_from_pressure()
    machineTemp = cpuTemp()

    temp = (temperature1+temperature2)/2
    accountForCPU = temp - ((machineTemp - temp)/1.5)
    temp = c_to_f(accountForCPU) 
   
    tempList.append(temp)
    tempList.pop(0)

    loopCount = loopCount % 5
    
    if(loopCount == 0):	
	avgTemp = 0
        for nums in tempList:
            avgTemp += nums
        avgTemp = avgTemp/len(tempList)

        riseOrDrop = lastTemp - avgTemp
        lastTemp = avgTemp

        if(riseOrDrop > 0):
            display.displayDrop(sense)
        else:
            display.displayRise(sense)


    pressure = sense.get_pressure()
    humidity = sense.get_humidity()

    payload = {
        'station_id': stationid,
        'temperature': temp,
        'humidity': humidity,
        'pressure': pressure
        #'latitude': None,
        #'longitude': None
    }

    r = requests.post(url, data=payload)
    print(r.text)
    #print datetime.datetime.now()
    #print 'Temperature = %.1f Pressure = %.1f Humidity = %.1f' % (finalTemp, pressure, humidity)
    loopCount += 1
    time.sleep(30)


    #OpenWeatherAPI Use get to store data that we do not have access to.
    #Add more display
    #Clean up everything else.
    #Execute on startup
