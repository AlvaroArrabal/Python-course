from random import randint

class Person:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

class Client(Person):
    def __init__(self,name, surname,accountNumber, cash):
        super().__init__(name,surname)
        self.accountNumber = accountNumber
        self.cash = cash
    
    def __str__(self):
        return f"Client: {self.name} {self.surname}, Account Number: {self.accountNumber}, Current Cash: {self.cash}"
    
    def deposite(self,money):
        self.cash += money
    
    def retire(self,money):
         if money > client.cash:
            print("Sorry you don\'t have enough money")
         else:
            self.cash -= money


def new_client():
    print("Welcome!")
    clientName = input("What's your name: ")
    clientSurname = input("What's your surname: ")
    clientNumber = randint(10000,100000)
    clientCash = input("How much money do you have right now? ")

    return Client(clientName,clientSurname,clientNumber,float(clientCash))

def menu():
    print(" 1. Information\n 2. Deposite\n 3. Retire\n 4. Exit")
    option = input("Option: ") 
    return int(option)


client = new_client()

option = menu()
while option != 4:
    if option == 1:
        print(client)
    elif option == 2:
        money = input("How mucho money do you want to deposite?")
        client.deposite(float(money))
    elif option == 3:
        money = input("How mucho money do you want to retire?")
        money = float(money)
        client.retire(money)
    option = menu()