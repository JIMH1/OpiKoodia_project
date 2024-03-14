#from torstaiDB import getPlayer, savePlayer
import datetime
import random
from time import sleep
import sqlite3
import RPi.GPIO as GPIO
from gpiozero import LED, Button
import os

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(2,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

connection = sqlite3.connect('torstai.db')
cursor = connection.cursor()


cursor.execute('''
  CREATE TABLE IF NOT EXISTS torstai (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    points INTEGER,
    gameID INTEGER,
    date TEXT
  );
''')

def savePlayer(name, score):
  cursor.execute('INSERT INTO torstai (name, points) VALUES (?, ?)', (name, score))
  connection.commit()


def getPlayer(name):
  cursor.execute('SELECT * FROM torstai WHERE name = ?', (name,))#ei toimi, jos ei oo tuota commaa tossa
  playerData = cursor.fetchone()
  return playerData

def getAll():
  cursor.execute('SELECT * FROM torstai')
  data = cursor.fetchall()
  return data
  
def getHighScore():
    cursor.execute('SELECT * FROM torstai ORDER BY points ASC LIMIT 1')
    data = cursor.fetchone()
    return data

def getLast():
    cursor.execute('SELECT * FROM torstai ORDER BY id DESC LIMIT 1')
    data = cursor.fetchone()
    return data

def buttonPressed(btn):
    turnOffLed()

def playGameOne():
  #print("Welcome to game one")
  #tässä muka tapahtuis jotain pelilogiikkaa
    
#Keltanen on kakkonen
    #oranssi on kolme
  led = LED(3)
  button = Button(2)
  
  led.off()
  led.on()
  sleep(1)#ledin syttyminen vaatii jostian syystä sleepin
  led.off()
  
  print("All scores")
  print(getAll())
  print("hi score")
  print(getHighScore())
  print("viimeisin")
  print(getLast())
    #getAll()
  
  points = {}
  player = input("Give your name ")
  points[player] = 0
  rounds = int(input("Rounds: "))
    
  for r in range(0, rounds):
    sleep(0.5)
    print("Get ready..")
    #lamppu vilkkuu?
    led.off()
    led.on()
    sleep(1)
    led.off()
    led.on()
    sleep(1)
    led.off()
    
    
    sleep(random.randint(1,3))
    #lamppu syttyisi
    led.on()
    
    then = datetime.datetime.now()
    
    
    t = input("GO!! ")
    #lamppu sammmuis tässä
    led.off()
    
    now = datetime.datetime.now()
    
    
    diff = then-now
    
    reaction_time = round(abs(diff.total_seconds()), 2)
    print("Reaction time: {} seconds".format(reaction_time))
        
    savePlayer(player, reaction_time)
  
  sleep(0.5)
  led.off()
  
  #tehään neljä muuttujaa, jotka tallennetaan torstaiDBn avulla kantaan
  #player = input("Pls give me a name")#stringi
  #playerScore = input("Pls give me a score")#intti, mut kannassa stringi?
  #Koitetaan tallentaa kantaan tiedot
  


  #Check jos tiedot löytyy kannasta
  #testData = getPlayer(playerName)
  #print(testData)


playGameOne()

test = getAll()
print(test)

connection.close()
