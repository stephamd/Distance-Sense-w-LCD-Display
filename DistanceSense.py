
#!/usr/bin/python
#
# Distance Sense with LCD Display realtime
# Raspberry Pi
#
# Author : Matt Stephan
# site   : github.com/stephamd
# Date   : 02/06/2016
#

import RPi.GPIO as GPIO
import time

import HC_SR04_Driver
#import  LCD_Driver



def main():
  	


	#GPIO DEBUG:Scanning for a 1

	#gpioScan(6,1)
	
	#print "\033[2J"
	print "Distance Sensor"
	print "*********************************"

	distSensor = HC_SR04_Driver.HCSensorModule(19,6)

  	sensorTimeStart = time.time()
  	
  	while(deltaT(sensorTimeStart) < 10):
		distSensor.measure()
		time.sleep(.2)
	
	
    	print "Done measuring. Measure time" , deltaT(sensorTimeStart)

    	GPIO.cleanup()


def deltaT(start):
	deltaTime = time.time()-start
	return deltaTime

def gpioScan(pin,binary):
	while True:
		if GPIO.input(pin) == binary:
			print "GPIO is 1 ", time.time()
			return

if __name__ == '__main__':
  main()
