from time import sleep, time
import datetime
import random
import RPi.GPIO as GPIO
import sqlite3

#DEFINITIONS, CONSTANTS
delay = 0.1
redLed = 40
yellowLed = 38
blueLed = 36

resetButton = 31

firstButton = 37
secondButton = 35
thirdButton = 33

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
def savePlayerReact(nimi, pojot):
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
    
def getPlayerReact(nimi):
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

def highScoreReact(määrä):
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()

    cursor.execute('SELECT name, MAX(points) from test GROUP BY name ORDER BY points DESC LIMIT ?', (määrä,) )
    data = cursor.fetchall()

    connection.close()
    return data
    
#94-133 uutta matskua, täytyy muuttaa funkkarien kutsut peleissä
def savePlayerScore(game, player_name, points, date):
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    
    # Create table for the game if it doesn't exist
    cursor.execute(f'''
      CREATE TABLE IF NOT EXISTS {game} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        points INTEGER,
        date TEXT
      );
    ''')
    
    cursor.execute(f'INSERT INTO {game} (name, points, date) VALUES (?, ?, ?)', (player_name, points, date))
    connection.commit()
    
    connection.close()
    
def getPlayerScore(game, player_name):
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    
    cursor.execute(f'SELECT * FROM {game} WHERE name = ?', (player_name,))
    playerData = cursor.fetchone()
    
    connection.close()
    return playerData

def getHighScores(game, limit):
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()

    cursor.execute(f'SELECT name, MAX(points) FROM {game} GROUP BY name ORDER BY points DESC LIMIT ?', (limit,))
    data = cursor.fetchall()

    connection.close()
    return data

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
    return random.choice(["EBA", "ABE", "AKU", "TIM", "BOB", "SAM", "IKE", "ÅKE", "OBI", "LEE", "MOE"])

def timeToPoints():#logiikka puuttuu
    points = random.choice([50, 100, 150, 200, 250])
    return points

def playReaction(playerName):
    
    print(f"Welcome to reaction, {playerName}")
    
    while True:
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
                    sleep(delay)
                    sleep(1)
                    time = endTime - startTime
                    score = timeToPoints()
                    print(score)
                    savePlayerReact(playerName, str(score))
                    return
                    break
            
        elif GPIO.input(secondButton) == 0 and randomLed == yellowLed:#and randomLed == outpin2
                if GPIO.input(secondButton) == 1:
                    
                    print("button pressed, turning off led")
                    sleep(delay)
                    turnOffLed(randomLed)
                    
                    endTime = datetime.datetime.now()
                    print(f"ending game{endTime}")
                    sleep(1)
    
                    time = endTime - startTime
                    score = timeToPoints()
                    print(score)
                    savePlayerReact(playerName, score)
                    return
                    break
                
        elif GPIO.input(thirdButton) == 0 and randomLed == blueLed:#and randomLed == outpin2
                if GPIO.input(thirdButton) == 1:
                    
                    print("button pressed, turning off led")
                    sleep(delay)
                    turnOffLed(randomLed)
                    
                    endTime = datetime.datetime.now()
                    print(f"ending game{endTime}")
                    sleep(1)
    
                    time = endTime - startTime
                    score = timeToPoints()
                    print(score)
                    savePlayerReact(playerName, score)
                    return
                    break
            
        
    print("outside loop")
    sleep(1)
    savePlayerReact(playerName, str(score))
    data = getPlayerReact(playerName)
    print(data)
    
#MAIN MENU LOGIC
def mainMenu():
    print("Welcome to the main menu of opikoodia Kokkola")
    print("Pls choose game by pressing a button 1 = reaction 2 = simon 3 = placeholder 4 = exit ")
    print("Since we dont have a keyboard, we will randomly assign you a name")
    playerName = generateName()
    print(f"your name is {playerName}")
    sleep(delay)
    
    data = getPlayerReact(playerName)
    print(data)
    
    
    while True:
        
        sleep(delay)
        print("choose game...")

        #DEBUGGING
        sleep(delay)
        readVal1 = GPIO.input(firstButton)
        print(readVal1)
        readVal2 = GPIO.input(secondButton)
        print(readVal2)
        readVal3 = GPIO.input(thirdButton)
        print(readVal3)
        readVal4 = GPIO.input(resetButton)
        print(readVal4)
        
        sleep(0.05)
        
        
        
        if readVal1 == 0:
 
            sleep(delay)
            #menuReact()
            playReaction(playerName)
            #print("react")
            sleep(delay)
        elif readVal2 == 0:
            #menuSimon()
            playSimonSays(playerName)
            #print("simon")
            sleep(delay)
        elif readVal3 == 0:
            menuPlaceholder()
            #playThirdGame(playerName)
            print("placeholder")
            sleep(delay)
        elif readVal4 == 0:
            print("exiting")
            #return #TÄTÄ vois testata 

#GAME TWO LOGIC
def playSimonSays(playerName):
    print(f"Welcome to simon says, {playerName}")
    
    mistakes = 0
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
        print("YES!!!")
        #speedUp(speed, minSpeed)#TOIMIIKO?
        sleep(2)
        return True
    else:
        print("NO!!!")
        #speedUp(speed, minSpeed)
        sleep(2)
        return False
    
def setupGPIO(redLed, yellowLed, blueLed, firstButton, secondButton, thirdButton, resetButton):
    GPIO.setup(redLed, GPIO.OUT)
    GPIO.setup(yellowLed, GPIO.OUT)
    GPIO.setup(blueLed, GPIO.OUT)

    GPIO.setup(firstButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(secondButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(thirdButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(resetButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def menuPlaceholder(name):
    while True:
        print("choose 1 for game, 2 for personalHigh, 3 for highScore...")
        
        readVal1 = GPIO.input(firstButton)
        readVal2 = GPIO.input(secondButton)
        readVal3 = GPIO.input(thirdButton)

        if readVal1 == 0:
            playPlaceholder(name)
            sleep(delay)
            return
            
        elif readVal2 == 0:
            playerData = getPlayerPlaceholder(nimi)
            print(playerData)
            sleep(delay)
            return
            
        elif readVal3 == 0:
            hiScoreData = highScorePlaceholder()
            print(hiScoreData)
            sleep(delay)
            return




def playPlaceholder(playerName):
    print(f"welcome to placeholder, {playerName}")
    sleep(5)
    return

def getPlayerPlaceholder(playerName):
    #SQL LOGIC
    print(f"successfully entered second test branch, {playerName}")
    sleep(5)
    return

def highScorePlaceholder():
    #SQL happens here
    print(f"successfully entered third test branch")
    sleep(5)
    return
mainMenu()
