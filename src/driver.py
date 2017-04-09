from sense_hat import SenseHat
import display
import time
import os
#import pymysql.cursors
#import sqlCommands
import datetime

################## Functions #######################################

def c_to_f(input):
    return (input*9/5)+32

def cpuTemp():
    reading = os.popen("vcgencmd measure_temp").readline()
    temp = float(reading.replace("temp=","").replace("'C\n",""))
    return(temp)

################# Database Connection ##############################
#db = pymysql.connect(host="server IP address goes here",
                    # user="username goes here",
                    # password="password goes here",
                    # db="database name goes here",
                    # charset='utf8mb4',
                    # cursorclass=pymysql.cursors.DictCursor)

################# SenseHat Objects ################################
sense = SenseHat()
sense.set_rotation(180)


################ Variables ########################################
riseOrDrop = 0
loopCount = 0
lastTemp = 0


############### "Main" Execution ####################################
while True:

    temperature1 = sense.get_temperature_from_humidity()
    temperature2 = sense.get_temperature_from_pressure()
    machineTemp = cpuTemp()

    avgTemp = (temperature1+temperature2)/2
    accountForCPU = avgTemp - ((machineTemp - avgTemp)/1.5)
    avgTemp = c_to_f(accountForCPU)

    riseOrDrop = lastTemp - avgTemp
    lastTemp = avgTemp
    loopCount = loopCount % 10
    if(loopCount == 0):
        if(riseOrDrop > 0):
            display.displayDrop(sense)
        else:
            display.displayRise(sense)


    pressure = sense.get_pressure()
    humidity = sense.get_humidity()


    #sqlCommands.write(db, datetime.datetime.now(), avgTemp, humidity, pressure)
    print datetime.datetime.now()
    print 'Temperature = %.1f Pressure = %.1f Humidity = %.1f' % (avgTemp, pressure, humidity)
    loopCount += 1
    time.sleep(5)
