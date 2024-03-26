from time import sleep, time
import datetime
import random
import RPi.GPIO as GPIO
import sqlite3

from RPLCD.gpio import CharLCD
#from RPLCD.i2c import CharLCD
from RPi import GPIO

lcd = CharLCD(cols=16, rows=2, pin_rs=22, pin_e=18, pins_data=[16, 11, 12, 15], numbering_mode=GPIO.BOARD)
#lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)


#DEFINITIONS, CONSTANTS
delay = 0.1
redLed = 37
yellowLed = 35
blueLed = 33

resetButton = 31

firstButton = 40
secondButton = 38
thirdButton = 36

GPIO.setmode(GPIO.BOARD)

#Funkkariks
GPIO.setup(redLed, GPIO.OUT)
GPIO.setup(yellowLed, GPIO.OUT)
GPIO.setup(blueLed, GPIO.OUT)

GPIO.setup(firstButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(secondButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(thirdButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(resetButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#funkkariks
GPIO.output(redLed, GPIO.LOW)
GPIO.output(yellowLed, GPIO.LOW)
GPIO.output(blueLed, GPIO.LOW)



ledStates = {
    redLed: False,
    yellowLed: False,
    blueLed: False,
}



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
    GPIO.output(ledPin, GPIO.HIGH)
    ledStates[ledPin] = True
    sleep(delay)
     
def turnOffLed(ledPin):
    GPIO.output(ledPin, GPIO.LOW)
    ledStates[ledPin] = False
    sleep(delay)
    
def toggleLed(ledPin):

    if ledStates[ledPin]:
        turnOffLed(ledPin)
    else:
        turnOnLed(ledPin)
    

    
def allLedOn():
    GPIO.output(redLed, GPIO.HIGH)
    GPIO.output(yellowLed, GPIO.HIGH)
    GPIO.output(blueLed, GPIO.HIGH)
    
def allLedOff():
    GPIO.output(redLed, GPIO.LOW)
    GPIO.output(yellowLed, GPIO.LOW)
    GPIO.output(blueLed, GPIO.LOW)
    
#GAMEONE LOGIC
def generateName():
    return random.choice(["EBA", "ABE", "AKU", "TIM", "BOB", "SAM", "IKE", "OBI", "LEE", "MOE"])

def timeToPoints(secs, micro):#logiikka puuttuu
    #points = random.choice([50, 100, 150, 200, 250])
    #relevantData = time[6:]

    secs = str(secs)
    micro = str(micro)
    return (secs +":"+ micro)
    
    #return points

def playReaction(playerName):
    lcd.clear()
    lcdPrint(f"Welcome, {playerName}", 0.1)#TOIMII
    print(f"Welcome to reaction, {playerName}")
    
    while True:
      lcdPrint("When alight,\n\rpress button", 0.1)#TOIMII
      randomLed = random.choice([redLed, yellowLed, blueLed])
      
      turnOnLed(randomLed)
      sleep(delay)
            
      startTime = datetime.datetime.now()

      print(f"start time {startTime}")
      sleep(delay)
      
      while True:
        if GPIO.input(firstButton) == 0 and randomLed == redLed:
            
            if GPIO.input(firstButton) == 1:
                    
                    print("button pressed, turning off led")
                    sleep(delay)
                    turnOffLed(randomLed)
                    
                    endTime = datetime.datetime.now()
                    print(f"ending game{endTime}")
                    #lcdPrint(f"Score: \n\r{endTime}", 2)
                    sleep(delay)
                    sleep(1)
                    time = endTime - startTime
                    seconds = time.seconds
                    mic = time.microseconds
                    score = timeToPoints(seconds, mic)
                    print(score)
                    #lcdPrint(f"Score: \n\r{score}", 2)
                    lcdPrint(f"Score: \n\r{score} secs", 5)
                    savePlayer(playerName, str(score))
                    return
                    break
            
        elif GPIO.input(secondButton) == 0 and randomLed == yellowLed:#and randomLed == outpin2
                if GPIO.input(secondButton) == 1:
                    
                    print("button pressed, turning off led")
                    sleep(delay)
                    turnOffLed(randomLed)
                    
                    endTime = datetime.datetime.now()
                    print(f"ending game{endTime}")
                    #lcdPrint(f"Score: \n\r{endTime}", 2)
                    sleep(1)
    
                    time = endTime - startTime
                    
                    seconds = time.seconds
                    mic = time.microseconds
                    score = timeToPoints(seconds, mic)
                    print(score)
                    #lcdPrint(f"Score: \n\r{score}", 2)
                    lcdPrint(f"Score: \n\r{score} secs", 5)
                    savePlayer(playerName, score)
                    lcd.clear()
                    return
                    break
                
        elif GPIO.input(thirdButton) == 0 and randomLed == blueLed:#and randomLed == outpin2
                if GPIO.input(thirdButton) == 1:
                    
                    print("button pressed, turning off led")
                    sleep(delay)
                    turnOffLed(randomLed)
                    
                    endTime = datetime.datetime.now()
                    print(f"ending game{endTime}")
                    #lcdPrint(f"Score: \n\r{endTime}", 2)
                    sleep(1)
    
                    time = endTime - startTime
                    seconds = time.seconds
                    mic = time.microseconds
                    score = timeToPoints(seconds, mic)
                    print(score)
                    #lcdPrint(f"Score: \n\r{score}", 2)
                    lcdPrint(f"Score: \n\r{score} secs", 5)
                    savePlayer(playerName, score)
                    return
                    break
            
        
    print("outside loop")
    sleep(1)
    savePlayer(playerName, str(score))
    data = getPlayer(playerName)
    print(data)
    
#MAIN MENU LOGIC
def mainMenu():
    lcd.clear()
    lcdPrint("Welcome to the \n\rmain menu of \n\r team Kokkola \n\rproject", 0.1)#TOIMII
    print("Welcome to the main menu of opikoodia Kokkola")
    
    playerName = generateName()
    lcdPrint(f"Your name \n\ris {playerName}", 0.1)#TOIMII
    print("Since we dont have a keyboard, we will randomly assign you a name")
    
    
    print(f"your name is {playerName}")
    
    sleep(delay)
    
    data = getPlayer(playerName)
    print(data)
    
    
    while True:
        
        sleep(delay)
        
        lcdPrint("Choose by\n\rpressing buttons", 0.1)#TOIMII
        print("Pls choose game by pressing a button 1 = reaction 2 = simon 3 = placeholder")
        lcdPrint("1 for react\n\r2 for simon", 0.1)#TOIMII
        #lcdPrint("3 for X", 2)
        
        sleep(delay)
        readVal1 = GPIO.input(firstButton)
        print(readVal1)
        readVal2 = GPIO.input(secondButton)
        print(readVal2)
        readVal3 = GPIO.input(thirdButton)
        print(readVal3)
        
        sleep(0.05)
        
        
        
        if readVal1 == 1:
 
            sleep(delay)
            playReaction(playerName)
            #print("react")
            sleep(delay)
        elif readVal2 == 1:
            playSimonSays(playerName)
            #print("simon")
            sleep(delay)
        elif readVal3 == 1:
            #playThirdGame(playerName)
            print("placeholder")
            sleep(delay)


#GAME TWO LOGIC
def playSimonSays(playerName):
    lcdPrint(f"Welcome to simon\n\r{playerName}", 0.1)#TOIMII
    print(f"Welcome to simon says, {playerName}")
    
    
    mistakes = 1
    limit = 2
    speed = 2
    minSpeed = 0.5
    
    ledArr = [redLed, yellowLed, blueLed]
    buttonArr = [firstButton, secondButton, thirdButton]
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
    
    lcdPrint("kiitos pelista", 3)
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
                if GPIO.input(button) == GPIO.HIGH:#pud_updown#täÄÄ OLI LOW
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
        firstButton: redLed,
        secondButton: yellowLed,
        thirdButton: blueLed
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
        firstButton: redLed,
        secondButton: yellowLed,
        thirdButton: blueLed
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
        lcdPrint("YES!!!", 1)
        print("YES!!!")
        #speedUp(speed, minSpeed)#TOIMIIKO?
        sleep(2)
        return True
    else:
        lcdPrint("NO!!!", 1)
        print("NO!!!")
        #speedUp(speed, minSpeed)
        sleep(2)
        return False
    


###LCD RUUTU
def lcdPrint(teksti, kesto):
    if len(teksti) > 32:
        alku = teksti[0:32]
        häntä = teksti[33:]
        
        lcd.clear()
        lcd.write_string(alku)
        sleep(kesto)
        lcd.clear()
        
        lcdPrint(häntä, kesto)
    else:
        lcd.clear()
        lcd.write_string(teksti)
     
        sleep(kesto)
        lcd.clear()
        return
    


mainMenu()
