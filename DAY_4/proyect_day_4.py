from random import *

print("/-------------------------------------------------------\\")
print(" Hello! Do you want to play with me?")
name = input(" Okey! Whats your name? ")
print(f"\n Okey {name}, you have 8 tries to guess my number jeje\nThe number is between 0 and 100\nLets Begin!")
print("\\-------------------------------------------------------/")
N = randint(0,100)

win = False

n = 1
while n<=8:
    number = input(f" attempt number {n}: ")
    number = int(number)
    if number < 0 or number >100:
        print(" Thats a wrong number, you lost a trie!")
    elif number > N:
        print(" Ups! Your number is higher...")
    elif number < N:
        print(" Ups! Your number is lower...")
    elif number == N:
        print(f" OH! You win! Congratulations {name}!")
        if n <= 2:
            print(f" You needed {n} attempts, amazing!")
        elif n <= 4:
            print(f" You needed {n} attempts, Very well!")
        elif n <= 6:
            print(f" You needed {n} attempts, not bad")
        else:
            print(f" You needed {n} attempts, that was close")
        win = True
        break
    n +=1

if win == False:
    print(f" You lost... The number was {N}... good luck next time!")

print("/-------------------------------------------------------\\")
print(" Thanks for playing :)")
print("\\-------------------------------------------------------/")