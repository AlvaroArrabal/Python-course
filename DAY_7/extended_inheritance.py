class Father:
    def talk(self):
        print("Hello!")

class Mother:
    def laughter(self):
        print("Ja Ja!")

    def talk(self):
        print("How are you?")

class Son(Father, Mother):          
    pass

class Grandson(Son):
    pass



myGrandson = Grandson()

myGrandson.talk()                   # Mother and Father have a function with the same name, the grandson will say Hello! because he/she inherited it from his/her father before his/her mother
myGrandson.laughter()

print(Grandson.__mro__)             # prints the order of inheritance