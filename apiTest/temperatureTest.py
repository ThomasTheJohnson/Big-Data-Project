import os
from sense_hat import SenseHat
import time

#def getCPUtemperture():
#	res = os.popen('vcgencmd measure_temp').readline()
#	print res
#	return(res.replace("temp=","").replace("'C\n",""))

#CPU_temp = getCPUtemperture()
#print CPU_temp

def c_to_f(input):
	return (input*9/5)+32
sense = SenseHat()
sense.set_rotation(180)
while True:
	pressure = sense.get_pressure()
	temp = sense.get_temperature()
	humidity = sense.get_humidity()
	calctemp = 0.0071*temp*temp+0.86*temp-10.0
	temp = c_to_f(calctemp)
	tempstr = str(temp)
	sense.show_message(tempstr, .05, [255,255,255],[0,0,0])
	calchum = humidity*(2.5-0.029*temp)
	print 'Pressure = %.0f Temperature = %.1f Humidity = %.0f' % (pressure, temp, calchum)
	time.sleep(5)

