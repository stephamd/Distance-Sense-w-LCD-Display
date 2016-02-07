
#!/usr/bin/python
#
# Distance Sense with LCD Display realtime
# Raspberry Pi
#
# Author : Matt Stephan
# site: github.com/stephamd
# Date   : 02/06/2016
#

import RPi.GPIO as GPIO
import time
import HC_S04_Driver
import LCD_Driver



def main():
  
  print "Welcome to Distance Sensor"
  distSensor = HC_S04_Driver.sensor(5,6)
  
  sensorTime = time.time()
  
  while(sensorTime >10)
    print distSensor.measure()
    
  print "Done measuring. Measure time" , sensorTime
    
  GPIO.cleanup()
  




if __name__ == '__main__':
  main()
