# DRY -> Dont Repeat Yourself

class Animal:
    def __init__(self,age,color):
        self.age = age
        self.color = color

    def birth(self):
        print("This animal was born")

class Bird(Animal):
    def __init__(self, age, color,flight_altitude):
        super().__init__(age, color)                    # from class Animal
        self.flight_altitude = flight_altitude          # Particular attribute

    def fly (self):
        print("the Bird is flying")

class Dog(Animal):
    pass

print(Animal.__subclasses__())
print(Bird.__bases__)


myBird = Bird(2,"brown")
myBird.birth()