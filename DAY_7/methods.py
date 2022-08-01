class Bird:
    wings = True

    def __init__(self, color, species):
        self.color = color
        self.species = species

    def chirp(self):
        print(f"pio pio, my color is {self.color}")
    
    def fly(self,meters):
        print(f"the bird has flown {meters} meters")
        self.chirp()

    def turn_black(self):
        self.color = "black"
        print(f"Now the bird is {self.color}")

    @classmethod                                            
    def eggs(cls, quantity):
        print(f"The bird has {quantity} eggs")

    @staticmethod                                           
    def look():
        print("the bird look")



myBird = Bird("brown","sparrow")

Bird.look()