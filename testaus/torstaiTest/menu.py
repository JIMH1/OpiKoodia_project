from gameone import playGameOne
from gametwo import playGameTwo

print("welcome to the main menu")

playerChoice = input("please choose either 1 or 2")
#tässä käytännössä halutaan mennä joko game1 tai game2
if(playerChoice == 1):
  playGameOne()
elif(playerChoice == 2):
  playGameTwo()
else:
  print("Wrong input")