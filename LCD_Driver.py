#!/usr/bin/python
#
# HD44780 LCD Test Script for
# Raspberry Pi
#
# Author : Matt Stephan
# Site   : http://www.github.com/stephamd
# Class implementation by Matt Stephan
# Parts of code from Matt Hawkins
# Date   : 26/07/2012
#

# The wiring for the LCD is as follows:
# 1 : GND
# 2 : 5V
# 3 : Contrast (0-5V)*
# 4 : RS (Register Select)
# 5 : R/W (Read Write)       - GROUND THIS PIN
# 6 : Enable or Strobe
# 7 : Data Bit 0             - NOT USED
# 8 : Data Bit 1             - NOT USED
# 9 : Data Bit 2             - NOT USED
# 10: Data Bit 3             - NOT USED
# 11: Data Bit 4
# 12: Data Bit 5
# 13: Data Bit 6
# 14: Data Bit 7
# 15: LCD Backlight +5V**
# 16: LCD Backlight GND

#import
import RPi.GPIO as GPIO
import time

# Define GPIO to LCD mapping


class LCD_Driver:


        def __init__(self,rs,e,d4,d5,d6,d7):


                self.LCD_RS = rs #25
                self.LCD_E  = e #24
                self.LCD_D4 = d4 #23
                self.LCD_D5 = d5 #17
                self.LCD_D6 = d6 #21
                self.LCD_D7 = d7 #22

                # Define some device constants
                self.LCD_WIDTH = 16    # Maximum characters per line
                self.LCD_CHR = True
                self.LCD_CMD = False

                self.LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
                self.LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line 

                # Timing constants      
                self.E_PULSE = 0.00005
                self.E_DELAY = 0.00005

                GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers

                GPIO.setup(self.LCD_E, GPIO.OUT)  # E
                GPIO.setup(self.LCD_RS, GPIO.OUT) # RS
                GPIO.setup(self.LCD_D4, GPIO.OUT) # DB4
                GPIO.setup(self.LCD_D5, GPIO.OUT) # DB5
                GPIO.setup(self.LCD_D6, GPIO.OUT) # DB6
                GPIO.setup(self.LCD_D7, GPIO.OUT) # DB7

                # Initialise display
                self.lcd_byte(0x33,self.LCD_CMD)
                self.lcd_byte(0x32,self.LCD_CMD)
                self.lcd_byte(0x28,self.LCD_CMD)
                self.lcd_byte(0x0C,self.LCD_CMD)
                self.lcd_byte(0x06,self.LCD_CMD)
                self.lcd_byte(0x01,self.LCD_CMD)


    def updateLine(self, lineNum, textStr):

                if lineNum == 1:
                        self.lcd_byte(self.LCD_LINE_1, self.LCD_CMD)
                        self.lcd_string(textStr)
                        return 1

                if lineNum == 2:
                        self.lcd_byte(self.LCD_LINE_2, self.LCD_CMD)
                        self.lcd_string(textStr)
                        return 1

                print "Invalid line number. 1 or 2"
                return -1


        def lcd_string(self, message):
                # Send string to display

                message = message.ljust(self.LCD_WIDTH," ")

                for i in range(self.LCD_WIDTH):
                        self.lcd_byte(ord(message[i]),self.LCD_CHR)

 def lcd_byte(self, bits, mode):
                # Send byte to data pins
                # bits = data
                # mode = True  for character
                #        False for command

                GPIO.output(self.LCD_RS, mode) # RS

                # High bits
                GPIO.output(self.LCD_D4, False)
                GPIO.output(self.LCD_D5, False)
                GPIO.output(self.LCD_D6, False)
                GPIO.output(self.LCD_D7, False)
                if bits&0x10==0x10:
                        GPIO.output(self.LCD_D4, True)
                if bits&0x20==0x20:
                        GPIO.output(self.LCD_D5, True)
                if bits&0x40==0x40:
                        GPIO.output(self.LCD_D6, True)
                if bits&0x80==0x80:
                        GPIO.output(self.LCD_D7, True)

                # Toggle 'Enable' pin
                time.sleep(self.E_DELAY)
                GPIO.output(self.LCD_E, True)
                time.sleep(self.E_PULSE)
                GPIO.output(self.LCD_E, False)
                time.sleep(self.E_DELAY)

 # Low bits
                GPIO.output(self.LCD_D4, False)
                GPIO.output(self.LCD_D5, False)
                GPIO.output(self.LCD_D6, False)
                GPIO.output(self.LCD_D7, False)

                if bits&0x01==0x01:
                        GPIO.output(self.LCD_D4, True)
                if bits&0x02==0x02:
                        GPIO.output(self.LCD_D5, True)
                if bits&0x04==0x04:
                        GPIO.output(self.LCD_D6, True)
                if bits&0x08==0x08:
                        GPIO.output(self.LCD_D7, True)

                # Toggle 'Enable' pin
                time.sleep(self.E_DELAY)
                GPIO.output(self.LCD_E, True)
                time.sleep(self.E_PULSE)
                GPIO.output(self.LCD_E, False)
                time.sleep(self.E_DELAY)

if __name__ == '__main__':
  main()








