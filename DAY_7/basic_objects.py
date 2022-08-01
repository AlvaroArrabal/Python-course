class Bird:

    wings =True                                 # global attribute

    def __init__(self, color, species):
        self.color = color
        self.species = species


myBird = Bird("brown","sparrow")

print(myBird.color)
print(myBird.species)

print(Bird.wings)
print(myBird.wings)