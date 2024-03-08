#from pyfirmata import Arduino, util
import time
import random
from pyfirmata import Arduino, util

redLedPin = 12
orangeLedPin = 11
blueLedPin = 10

buttonOnePin = 7

board = Arduino('/dev/ttyACM0')

it = util.Iterator(board)#Magic
it.start()

redLed = board.get_pin('d:' + str(redLedPin) + ':o')#magic
orangeLed = board.get_pin('d:' + str(orangeLedPin) + ':o')#magic
blueLed = board.get_pin('d:' + str(blueLedPin) + ':o')#magic
buttonOne = board.get_pin('d:' + str(buttonOnePin) + ':i')#magic

def blinkRedLed():
    redLed.write(1)
    time.sleep(1)
    redLed.write(0)
    time.sleep(1)

def blinkOrangeLed():
    orangeLed.write(1)
    time.sleep(1)
    orangeLed.write(0)
    time.sleep(1)

def blinkBlueLed():
    blueLed.write(1)
    time.sleep(1)
    blueLed.write(0)
    time.sleep(1)
    

def redLedOn():
    redLed.write(1)
    time.sleep(1)

def redLedOff():
    redLed.write(0)
    time.sleep(1)
    

def orangeLedOn():
    orangeLed.write(1)
    time.sleep(1)

def orangeLedOff():
    orangeLed.write(0)
    time.sleep(1)
    

def blueLedOn():
    blueLed.write(1)
    time.sleep(1)

def blueLedOff():
    blueLed.write(0)
    time.sleep(1)
    
def allOn():
    redLed.write(1)
    orangeLed.write(1)
    blueLed.write(1)
    
def allOff():
    redLed.write(0)
    orangeLed.write(0)
    blueLed.write(0)

def readyBlink():
    blinkRedLed()
    blinkOrangeLed()
    blinkBlueLed()

def waitRandomTime():
    time.sleep(random.uniform(1, 3))
    
def cycleSuspense():
    redLed.write(1)
    time.sleep(0.3)
    orangeLed.write(1)
    time.sleep(0.3)
    blueLed.write(1)
    time.sleep(0.3)
    
    allOff()
    
def lightLed(time):
    if time < 1:
        blueLed.write(1)
    elif time < 2:
        orangeLed.write(1)
    else:
        redLed.write(1)

def announceTime(time):
    print("Your time was #{time}")
    
while True:
    allOff()
    
    while buttonOne.read() == 0:#AND !game_started
        readyBlink()
        

    while buttonOne.read() == 1:
        pass
    
    waitRandomTime()
    allOn()
    startTime = time.time()
    
    #eventti napin painamiselle
    while buttonOne.read() == 0:#pikemminki !pressed(buttonOne)
        pass
    
    allOff()
    endTime = time.time()
    
    reactionTime = (endTime - startTime)
    
    cycleSuspense()
    lightLed(reactionTime)
    announceTime(reactionTime)



