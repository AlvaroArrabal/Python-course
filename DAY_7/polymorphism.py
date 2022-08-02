class Cow:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(self.name + " , Muu")

class Sheep:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(self.name + " , Bee")


cow1 = Cow("Arthur")
sheep1 = Sheep("Alfred")


cow1.talk()
sheep1.talk()

# Same function name but each one does different things


animals = [cow1,sheep1]

for i in animals:
    i.talk()

def animal_talk(animal):
    animal.talk()

animal_talk(cow1)
animal_talk(sheep1)