
if 5<6:
    print("hello!")
else:
    print("bye!")

x = False

if x:
    print("Its True!")
else:
    print("Thats false :(")


pet = "Dog"

if pet == "Cat":
    print("You have a cat")
elif pet == "Dog":
    print("You have a Dog!")
else:
    print("I dont know which animal do you have :(")


age = 23
sex = "male"

if age == 23 and sex == "male":
    print("You are 23 years old")

if age == 23:
    if sex == "male":
        print("You are a man")
    else:
        print("You are a women")
else:
    print("How old are you?")