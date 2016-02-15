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
import  LCD_Driver



def main():



        #GPIO DEBUG:Scanning for a 1

        #gpioScan(6,1)

        #print "\033[2J"
        print "Distance Sensor"
        print "*********************************"

        distSensor = HC_SR04_Driver.HCSensorModule(19,6)

        lcd = LCD_Driver.LCD_Driver(25,24,23,17,21,22)

        lcd.updateLine(1,"Distance Sense")
        lcd.updateLine(2,"Matt S")
        time.sleep(2)

        lcd.updateLine(1,"Meas. (cm)")
        lcd.updateLine(2,"")

        sensorTimeStart = time.time()

        try:
                while True:
                        meas = distSensor.measure()
                        lcd.updateLine(2, str(meas))
                        time.sleep(.25)

        except KeyboardInterrupt:
                pass


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

