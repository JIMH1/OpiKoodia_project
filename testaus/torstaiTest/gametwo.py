from torstaiDB import getPlayer, savePlayer

def playGameTwo():
  print("Welcome to game two")
  #tässä muka tapahtuis jotain pelilogiikkaa

  #tehään neljä muuttujaa, jotka tallennetaan torstaiDBn avulla kantaan
  playerName = input("Pls give me a name")#stringi
  playerScore = input("Pls give me a score")#intti, mut kannassa stringi?
  playerGame = input("Pls give me a gameID")#intti, mut tallennetaan kantaan stringinä?
  playerDate = input("Pls give a date")#stringi

  #Koitetaan tallentaa kantaan tiedot
  savePlayer(playerName, playerScore, playerGame, playerDate)

  #Check jos tiedot löytyy kannasta
  testData = getPlayer(playerName)
  print(testData)

