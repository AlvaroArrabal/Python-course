from random import *

def throw_dices():
    dice1 = 0
    dice2 = 0
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    print(dice1,dice2)
    return dice1,dice2

res1, res2 = throw_dices()
def check(dice1,dice2):
    res = dice1 + dice2
    print(res)
    if res <= 6:
        print(f"Your dice add up to {res}, poor")
    elif res > 6 and res < 10:
        print(f"Your dice add up to {res}, not bad")
    else:
        print(f"Your dice add up to {res}, good one")
    
    return res

check(res1,res2)