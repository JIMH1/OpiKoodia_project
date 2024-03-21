#ALLA OLEVA KOODI EI TOIMI SUORAAN


from time import sleep, time
import datetime
import random
import RPi.GPIO as GPIO
import sqlite3

#DEFINITIONS, CONSTANTS
delay = 0.1#
inpin1 = 40
outpin1 = 38
inpin2 = 37
outpin2 = 35

GPIO.setmode(GPIO.BOARD)

GPIO.setup(outpin1, GPIO.OUT)
GPIO.setup(outpin2, GPIO.OUT)

GPIO.setup(inpin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)#up vai dwon
GPIO.setup(inpin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)#

GPIO.output(outpin1, GPIO.LOW)
GPIO.output(outpin2, GPIO.LOW)

ledStates = {
    outpin1: False,
    outpin2: False,
    }

#ledState1 = False
#ledState2 = False

#SQL STUFF
def savePlayer(nimi, pojot):
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    
    cursor.execute('''
      CREATE TABLE IF NOT EXISTS test (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        points INTEGER
      );
    ''')
    
    
    
    cursor.execute('INSERT INTO test (name, points) VALUES (?, ?)', (nimi, pojot))
    connection.commit()
    
    connection.close()
    
def getPlayer(nimi):
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    
    cursor.execute('''
      CREATE TABLE IF NOT EXISTS test (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        points INTEGER
      );
    ''')
    
    cursor.execute('SELECT * FROM test WHERE name = ?', (nimi,) )
    playerData = cursor.fetchone()
    connection.close
    return playerData

#LEDSTUFF
def turnOnLed(ledPin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.HIGH)
    
def turnOffLed(ledPin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    
def toggleLed(ledPin):
    #ledState = not ledState
    #global ledState
    ledStates[ledPin] = not ledStates[ledPin]
    
    GPIO.output(ledPin, ledStates[ledPin])
    
    #if ledState:
    #    turnOnLed(ledPin)
    #else:
    #    turnOffLed(ledPin)
        
    sleep(delay)#ettei paina kahesti
    #return ledState ei tarvita enää

#GAMEONE LOGIC
def generateName():
    return random.choice(["EBA", "ABE", "AKU", "TIM", "BOB", "SAM", "IKE", "ÅKE", "OBI", "LEE", "MOE"])

def timeToPoints():#logiikka puuttuu
    points = random.choice([50, 100, 150, 200, 250])
    return points

def playReaction(playerName):
    inpin1 = 40
    outpin1 = 38
    inpin2 = 37
    outpin2 = 35

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(outpin1, GPIO.OUT)
    GPIO.setup(outpin2, GPIO.OUT)

    GPIO.setup(inpin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)#up vai dwon
    GPIO.setup(inpin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)#

    GPIO.output(outpin1, GPIO.LOW)
    GPIO.output(outpin2, GPIO.LOW)

    ledState1 = False
    ledState2 = False
    
    print(f"Welcome to reaction, {playerName}")
    
    
    while True:
      randomLed = random.choice([outpin1, outpin2])
      
      turnOnLed(randomLed)
      sleep(delay)
      
      
      startTime = datetime.datetime.now()
      print(f"start time {startTime}")
      sleep(delay)
      
      
      while True:
        if GPIO.input(inpin1) == 0 and randomLed == outpin1:#how about 1
            
            if GPIO.input(inpin1) == 1:
                    
                    print("button pressed, turning off led")
                    sleep(delay)
                    turnOffLed(randomLed)
                    
                    endTime = datetime.datetime.now()
                    print(f"ending game{endTime}")
                    sleep(delay)
                    sleep(1)
                    time = endTime - startTime
                    score = timeToPoints()
                    print(score)
                    savePlayer(playerName, str(score))
                    return
                    break
            
        elif GPIO.input(inpin2) == 0 and randomLed == outpin2:#and randomLed == outpin2
                if GPIO.input(inpin2) == 1:
                    
                    print("button pressed, turning off led")
                    sleep(delay)
                    turnOffLed(randomLed)
                    
                    endTime = datetime.datetime.now()
                    print(f"ending game{endTime}")
                    sleep(1)
    
                    time = endTime - startTime
                    score = timeToPoints()
                    print(score)
                    savePlayer(playerName, score)
                    return
                    break
            
        
    print("outside loop")
    sleep(1)
    savePlayer(playerName, str(score))
    asd = getPlayer(playerName)
    print(asd)
    
#MAIN MENU LOGIC
def mainMenu():
    print("Welcome to the main menu of opikoodia Kokkola")
    print("Pls choose game by pressing a button 1 = reaction 2 = simon")
    print("Since we dont have a keyboard, we will randomly assign you a name")
    playerName = generateName()
    print(f"your name is {playerName}")
    sleep(delay)
    
    asd = getPlayer(playerName)
    print(asd)
    
    
    while True:
        sleep(delay)
        print("choose game...")
        sleep(delay)
        readVal1 = GPIO.input(inpin1)
        readVal2 = GPIO.input(inpin2)
            
        if readVal1 == 0:
 
            sleep(delay)
            playReaction(playerName)
            sleep(delay)
        if readVal2 == 0:
            playSimonSays(playerName)
            sleep(delay)

#GAME TWO LOGIC
def playSimonSays(playerName):
    #print("debug 1")
    inpin1 = 40
    outpin1 = 38
    inpin2 = 37
    outpin2 = 35

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(outpin1, GPIO.OUT)
    GPIO.setup(outpin2, GPIO.OUT)

    GPIO.setup(inpin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)#up vai dwon
    GPIO.setup(inpin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)#

    GPIO.output(outpin1, GPIO.LOW)
    GPIO.output(outpin2, GPIO.LOW)

    ledState1 = False
    ledState2 = False
    
    #print("debug 2")
    
    print(f"Welcome to simon says, {playerName}")
    mistakes = 0
    limit = 2
    speed = 2
    minSpeed = 0.5
    
    ledArr = [outpin1, outpin2]
    buttonArr = [inpin1, inpin2]
    sequence = genSeq(ledArr)
    
    while mistakes < limit :
        
    

 
        
        print(sequence)#debug
    
        showSeq(sequence)#toimii, mut ehkä vois printata ledin värin debuggaamista varten
    
        buttonPresses = checkSeq(sequence, buttonArr)
        print(f"buttonPresses: {buttonPresses}")
        sleep(1)
    
        playerLeds = traslateButtonsToLed(buttonPresses)
        print(f"playerLeds: {playerLeds}")
        sleep(1)
    
        booleanVal = compareSeqs(sequence, playerLeds)
        print(booleanVal)
    
    
        if booleanVal:
            sequence = addToSeq(sequence, ledArr)
            print(sequence)
        else:
            
            mistakes += 1
    
    print("kiitos pelistä")
    #SQL stuff
    
def genSeq(ledArray): #length
    sequence = []
    first = random.choice(ledArray)
    second = random.choice(ledArray)
    
    sequence.append(first)    
    sequence.append(second)
    
    return sequence

def addToSeq(sequence, ledArray):
    newLed = random.choice(ledArray)
    sequence.append(newLed)
    
    return sequence
    
def showSeq(sequence): #speed
    speed = calcSpeed(len(sequence))
    
    for led in sequence:
        toggleLed(led)
        sleep(speed)#speed
        toggleLed(led)
        
     

def checkSeq(sequence, buttonArr):
    playerInput = []
    
    for buttonPress in range(len(sequence)):#buttonPress ei oo käytössä
        #tarvitaan looppi
        while True:
            print("inside loop, waiting for press")
            sleep(delay)
            sleep(delay)
            
            for button in buttonArr:#en keksi parmpaa tapaa chekata painalluksia
                print(playerInput)
                if GPIO.input(button) == GPIO.LOW:#pud_updown
                    playerInput.append(button)
                    
                    #Tää toimii vaan puoliks
                    #toggleLed(buttonToLed(button))
                    #sleep(delay)
                    #toggleLed(buttonToLed(button))
                    #sleep(delay)
                    
                    turnOnLed(buttonToLed(button) )
                    sleep(delay*2)
                    turnOffLed(buttonToLed(button) )
                    
                    sleep(delay)
                    
                    if len(playerInput) >= len(sequence):
                        print(f"exiting playerInput: {playerInput}")
                        
                        return playerInput
                        break
    sleep(1)
    
    print(playerInput)
    
    inputToLed = translateButtonsToLed(playerInput)
    osuma = (inputToLed == sequence)
    return osuma


def buttonToLed(button):
    
    buttonConnections = {
        inpin1: outpin1,
        inpin2: outpin2,
    }
    
    return buttonConnections[button]

def calcSpeed(length):
    if length == 2:
        return 2
    elif length == 3:
        return 1.5
    elif length == 4:
        return 1
    elif length == 5:
        return 0.5
    else:
        return 0.4

def traslateButtonsToLed(buttonPresses):
    #
    #print("inside translateFunc")
    buttonConnections = {
        inpin1: outpin1,
        inpin2: outpin2,
    }
    #sleep(1)
    #print("inside translateFunc2")
    #sleep(1)
    
    newArr = []
    
    for button in buttonPresses:
        newArr.append(buttonConnections[button])
    #print("inside translateFunc3")
    
    return newArr

def compareSeqs(sequence, playerSequence):
    if sequence == playerSequence:
        print("YES!!!")
        #speedUp(speed, minSpeed)#TOIMIIKO?
        sleep(2)
        return True
    else:
        print("NO!!!")
        #speedUp(speed, minSpeed)
        sleep(2)
        return False
    





mainMenu()
