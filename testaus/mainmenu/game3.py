import random
import mainmenu

def MENU():
    while True:
        print("\nWelcome to simon say game")
        print("1. Do you want to start to game")
        print("2. or go back")
        choice = int(input("Your number: "))
        if choice == 1:
            print("this is game 3")
        elif choice == 2:
            with open("mainmenu.py") as file:
                    exec(file.read())
        else:
            print("\nError! operator is not correct")

MENU()


