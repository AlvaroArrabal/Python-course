from random import *
def askLetter():
    letter = input("Insert a letter: ")
    return letter

def turn (secretWord, letter, res, win):
    cont =0
    for i in secretWord:
        if i == letter:
            res.pop(cont)
            res.insert(cont,letter)
        cont +=1
    aux = " ".join(res)
    print(aux)
    if "_" not in aux:
        return True
    else:
        return False
    
    


words = ["hello", "underground","car","home","table","computer","kitchen","fantasy","horse","wall"]

secretWord = choice(words)
res = list("_"*len(secretWord))
attemps = 6
win = False

print("-------------------------------------")
print("Hello! Welcome to my videogame\nReady to have fun? Lets go!")
print("-------------------------------------")
print("The game is easy, you have to guess the secret word!")
print("But be carefull, you only have 6 opportunities, so think well before you say a letter\nLets begin!")
print("This is the secret Word:")
aux = " ".join(res)
print(aux)


while attemps > 0:
    letter = askLetter()
    if letter in secretWord:
        print("Perfect!")
    else:
        attemps -= 1
        print(f"Nop :( You now have {attemps} attemps")
        
    win = turn(secretWord,letter,res,win)
    if win == True:
        break

if win == False:
    print(f"Sorry... but you lose...\n The secret Word was {secretWord}")

print("Congratulations! You win!")