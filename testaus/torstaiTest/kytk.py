from time import sleep, time
import datetime
import random
import RPi.GPIO as GPIO
import sqlite3


delay = 0.1#
redLed = 40
yellowLed = 38
blueLed = 36

resetButton = 37

firstButton = 31
secondButton = 33
thirdButton = 35


GPIO.setmode(GPIO.BOARD)

GPIO.setup(redLed, GPIO.OUT)
GPIO.setup(yellowLed, GPIO.OUT)
GPIO.setup(blueLed, GPIO.OUT)


GPIO.setup(firstButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)#up vai dwon
GPIO.setup(secondButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)#
GPIO.setup(thirdButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)#
GPIO.setup(resetButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)#

GPIO.output(redLed, GPIO.LOW)
GPIO.output(yellowLed, GPIO.LOW)
GPIO.output(blueLed, GPIO.LOW)




#LEDSTUFF

ledStates = {
    redLed: False,
    yellowLed: False,
    blueLed: False,
    }

def turnOnLed(ledPin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.HIGH)
    sleep(delay)
    
def turnOffLed(ledPin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    sleep(delay)
    
def toggleLed(ledPin):

    ledStates[ledPin] = not ledStates[ledPin]
    
    GPIO.output(ledPin, ledStates[ledPin])
    

        
    sleep(delay)#ettei paina kahesti
    

turnOnLed(redLed)
turnOnLed(yellowLed)
turnOnLed(blueLed)

while True:
    readVal1 = GPIO.input(firstButton)
    readVal2 = GPIO.input(secondButton)
    readVal3 = GPIO.input(thirdButton)
    
    if readVal1 == 0:
        turnOffLed(redLed)
        
    if readVal2 == 0:
        turnOffLed(yellowLed)
        
    if readVal3 == 0:
        turnOffLed(blueLed)
  
