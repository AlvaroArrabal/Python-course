from random import *                                        # import all from a library

ran = randint(1,50)
print(ran)

print("----------")

ran = uniform(1,50)                                         # returns a float
print(ran)

print("----------")

ran = random()                                              # 0 < ran < 1
print(ran)

print("----------")

colors = ["blue", "red", "pink","yellow", "green"]          # return a random value from a list
ran = choice(colors)
print(ran)

print("----------")

numbers = list(range(1,20))
shuffle(numbers)

print(numbers)