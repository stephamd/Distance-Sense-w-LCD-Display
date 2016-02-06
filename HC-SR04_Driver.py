#!/usr/bin/python
#
# HC-SR04 Driver Script for
# Raspberry Pi
#
# Author : Matt Stephan
#
# Date   : 02/06/2016
#

import RPi.GPIO as GPIO

import time

class HCSensorModule:
  
  def __init__ (self,t,e):
    
    self.trig_GPIO=t;  #define class variables for GPIO pins used for 
    selc.echo_GPIO=e;  #trigger and echo.
    
    #set gpio pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trig_GPIO,GPIO.OUT)
    GPIO.setup(echo_GPIO,GPIO.IN)
    
    GPIO.output(trig_GPIO,FALSE)
    print "HC Sensor Module Initialized"
    time.sleep(2)
    
  def measure():
    #Send out pulse
    GPIO.output(trig_GPIO, True)
    time.sleep(0.00001)
    GPIO.output(trig_GPIO, False)
    
    #listen for response
    timeCheckStart = time.time()
    
    while GPIO.input(echo_GPIO)==0
      timeCheckEnd = time.time()
      if timeCheckStart-timeCheckEnd  > 1
        print "bad read: did echo did not go low
        return
    #start pulse time once pin goes low
    pulseStart = time.time()
      
    while GPIO.input(echo_GPIO) == 1
    #end pulse time once pin goes high
    pulseEnd = time.time()
    #calculate pulse duration
    pulseTime = pulseStart-pulseEnd
    
    distance = calculateDistance(pulseTime)
    
    return distance
    
    
  def calculateDistance(pTime): #pass pulse time
    dist = 17150*pTime          #speed of sound is 34300cm/s. Divide by 2 for signal bounceback
    dist = round(dist,2)
    return dist
    
    















