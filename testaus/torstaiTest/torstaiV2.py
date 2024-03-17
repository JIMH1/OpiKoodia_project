from time import sleep, time
import datetime
import random
import RPi.GPIO as GPIO
import sqlite3

#DEFINITIONS, CONSTANTS
delay = 0.1#Tää oikeestaan vaan valoja varten, ehkä joku toinen delay esim tekstin syöttämistä varten
inpin1 = 40
outpin1 = 38
inpin2 = 37
outpin2 = 35

GPIO.setmode(GPIO.BOARD)

GPIO.setup(outpin1, GPIO.OUT)
GPIO.setup(outpin2, GPIO.OUT)

GPIO.setup(inpin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)#up vai down, voi asettaa downiksi, mutta se menee äkkiä hankalaksi seurata
GPIO.setup(inpin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)#

GPIO.output(outpin1, GPIO.LOW)
GPIO.output(outpin2, GPIO.LOW)

ledState1 = False
ledState2 = False

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
    
    
    
    cursor.execute('INSERT INTO test (name, points) VALUES (?, ?)', (nimi, pojot))#nää syötetään aina koneelle tupleina
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
    GPIO.setmode(GPIO.BOARD)#Nää toistot pitää jossai vaiheessa siivota
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.HIGH)
    
def turnOffLed(ledPin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    
def toggleLed(ledPin, ledState):
    ledState = not ledState
    
    if ledState:
        turnOnLed(ledPin)
    else:
        turnOffLed(ledPin)
        
    sleep(delay)#ettei paina kahesti
    return ledState

#GAMEONE LOGIC
def generateName():
    return random.choice([
    "ABE", "BEN", "CAM", "DAN", "EBA", "FAE", "GUS", "HAM", "IVY", "JAY", 
    "KIM", "LEO", "MIA", "NED", "OOT", "PAM", "QNC", "ROY", "SAM", "TOM",
    "UMA", "VAL", "WES", "XAV", "YEN", "ZOE", "ÅKE", "ÄTZ", "ÖRK"
])

def timeToPoints():#logiikka puuttuu, ATM arpoo random numeron. Vaihtoehtosesti syötetään kantaan stringinä tyyliin "mm:ss:ms"
    points = random.choice([50, 100, 150, 200, 250])
    return points

def playReaction(playerName):
    inpin1 = 40
    outpin1 = 38
    inpin2 = 37
    outpin2 = 35#NÄITÄ pitää laajentaa ja testata neljälle napille

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(outpin1, GPIO.OUT)
    GPIO.setup(outpin2, GPIO.OUT)

    GPIO.setup(inpin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)#up vai dwon
    GPIO.setup(inpin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)#

    GPIO.output(outpin1, GPIO.LOW)#pois päältä aluks
    GPIO.output(outpin2, GPIO.LOW)

    ledState1 = False
    ledState2 = False
    
    print(f"Welcome to reaction, {playerName}")
    
    
    while True:
      randomLed = random.choice([outpin1, outpin2])
      
      turnOnLed(randomLed)
      sleep(delay)#nää sleepit ledin jälkeen on tärkeitä
      
      startTime = datetime.datetime.now()
      print(f"start time {startTime}")
      sleep(delay)#eri delay tähä
      
      
      while True:
        if GPIO.input(inpin1) == 0 and randomLed == outpin1:#tarkistaa ettei nappi ole painettuna ja että on oikea nappi kyseessä
            #kun nappia painetaan(tai vissiin oikeesti kun nappi nostetaan ylös)
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
    
    asd = getPlayer(playerName)#printtaa kannasta aiempaa tietoa, jos on
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
    #set up variables
    #speed = 1
    #mistakes = 0

    greetPlayerSimon()
    explainRules()
    sequence = genSeq(3)

    while mistakes < 3:
        #main loop
            #after some time, remove 0.2 from speed
            #minimum = 0.3?

        showSeq(seq, speed)
        #player input
            #happy path:
                #addToSeq()
                #speedUp()
            #unhappy path:
                #increment mistakes,
                #show same sequence to player

    #once we exit the loop, save players score

def genSeq(length):
    seq = []
    for _ in range 0, length:
        randomLed = random.choice(ledList)
        seq.append(randomLed)
    
    return seq

def addToSeq(seq):
    randomLed = random.choice(ledList)
    seq.append(randomLed)

    return seq

def speedUp():
    pass

def playerInput(seqLength):
    pass


mainMenu()
