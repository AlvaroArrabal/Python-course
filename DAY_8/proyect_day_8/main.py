import turn
import os

def menu():

    while True:
        print("Choose one:\n  - Send\n  - Pick\n  - Information")
        try:
            option = input("Option: ").capitalize()
            ["Send","Pick","Information"].index(option)
        except ValueError:
            os.system("cls")
            print("Not valid option")
        else:
            break
    turn.welcome(option)


                
def begin():
    while True:
        os.system("cls")
        menu()
        try:
            another = input("Another turn: [Y] [N]\n").upper()
            ["Y","N"].index(another)
        except ValueError:
            print("Not valid option")
        else:
            if another == "N":
                print("Thank you for your visit")
                break

begin()