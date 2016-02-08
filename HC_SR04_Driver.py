#!/usr/bin/python
#
# HC-SR04 Driver Script for
# Raspberry Pi
#
# Author : Matt Stephan
# site   : github.com/stephamd
# Date   : 02/06/2016
#

import RPi.GPIO as GPIO

import time

class HCSensorModule:
  
	def __init__ (self,t,e):
    
		self.trig_GPIO=t;  #define class variables for GPIO pins used for 
		self.echo_GPIO=e;  #trigger and echo.
    		
		print "Trigger pin is GPIO ", t
		print "Echo pin is GPIO ", e

		#set gpio pins
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.trig_GPIO,GPIO.OUT)
		GPIO.setup(self.echo_GPIO,GPIO.IN)
    
		GPIO.output(self.trig_GPIO,0)
		time.sleep(2)
		print "HC Sensor Module Initialized"
    
	def measure(self):
		print "measure start..."
		

		self.gpioDebug()
	
		
		#Send out pulse
		GPIO.output(self.trig_GPIO, True)
		time.sleep(0.00001)
		GPIO.output(self.trig_GPIO, False)
		
    		timeCheck = time.time()
			
		#wait for beginning of pulse
		while (GPIO.input(self.echo_GPIO)==0):	
			if (time.time()-timeCheck  > 5):
				print "bad read:echo did not go low"
				return -1

		pulseStart = time.time()
      
		while (GPIO.input(self.echo_GPIO) == 1):
			pass

		pulseEnd = time.time()	

		#end pulse time once pin goes high
	
		#calculate pulse duration
		pulseTime = pulseEnd-pulseStart
    
		distance = self.calculateDistance(pulseTime)
    
		print "Distance: ", distance
    
    
	def calculateDistance(self, pTime): #pass pulse time
		dist = 17150*pTime          #speed of sound is 34300cm/s. Divide by 2 for signal bounceback
		dist = round(dist,2)
		return dist
    	def gpioDebug(self):
		print "GPIO: ",GPIO.input(self.echo_GPIO)
    


