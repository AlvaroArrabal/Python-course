
def add_send():
    for i in range(1,10000):
        yield f"S - {i}"
   
def add_pickUp():
    for i in range(1,10000):
        yield f"P - {i}"

def add_information():
    for i in range(1,10000):
        yield f"I - {i}"


s = add_send()
p = add_pickUp()
i = add_information()

def welcome(number):
    print("\n***********************\nYour turn is:")
    if number == "Send":
        print(next(s))
    elif number == "Pick":
        print(next(p))
    elif number == "Information":
        print(next(i))
    print("Thank you! Please wait\n***********************\n")
        



