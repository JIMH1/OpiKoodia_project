import random
from torstaiDB import getPlayer, savePlayer

def namePlayer():
  names = [
    "ABE", "BOB", "CAM", "DOT", "EVE", "FAE", "GUS", "HAL", "IKE", "JOE", "KIM", "LEE", "MOE", 
    "NAT", "OBI", "PAT", "QUN", "RIC", "SUE", "TOM", "ULA", "VIV", "WLT", "XIS", "YVE", "ZOE", 
    "ÅKE", "ÄKE, ÖKE"
  ]
  name = random.choice(names)
  return name

def namePlayerLoop():#tää tekee JOKAISEN combinaation ja valitsee yhen randomilla, aika overkill mut tuskin näin pienessä projektissa hirveesti väliä optimisaatiolla
  alph = "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ"
  names = []
  for c1 in alph:
    for c2 in alph:
      for c3 in alph:
        name = c1 + c2 + c3
        names.append(name)
        
        return random.choice(names)


def playGameOne():
  print("Welcome to game one")
  #tässä muka tapahtuis jotain pelilogiikkaa

  #tehään neljä muuttujaa, jotka tallennetaan torstaiDBn avulla kantaan
  playerName = namePlayer()
  playerScore = input("Pls give me a score")#intti, mut kannassa stringi?
  playerGame = input("Pls give me a gameID")#intti, mut tallennetaan kantaan stringinä?
  playerDate = input("Pls give a date")#stringi

  #Koitetaan tallentaa kantaan tiedot
  savePlayer(playerName, playerScore, playerGame, playerDate)

  #Check jos tiedot löytyy kannasta
  testData = getPlayer(playerName)
  print(testData)
