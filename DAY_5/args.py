from operator import add


def addition(*args):                # *args its for situations in which we dont know exactly how many arguments we have
    total = 0

    for i in args:
        total += i

    return total


print(addition(1,2,1,4,2,3,45,1))