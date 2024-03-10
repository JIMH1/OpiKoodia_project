import random
import game1
import game2
import game3


def MENU():
    while True:
        print("\nChoose your game")
        print("1. Reaction time game")
        print("2. Player vs player reaction game")
        print("3. Simons say")
        print("4. Close your app")
        choice = int(input("Your number: "))
        if choice == 1:
            with open("game1.py") as file:
                    exec(file.read())
        elif choice == 2:
            with open("game2.py") as file:
                    exec(file.read())
        elif choice == 3:
            with open("game3.py") as file:
                    exec(file.read())
        elif choice == 4:
            exit(0)
        else:
            print("\nError! operator is not correct")

MENU()