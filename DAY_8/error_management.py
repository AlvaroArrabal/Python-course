def addition():
    n1 = int(input("Number 1: "))
    n2 = int(input("Number 2: "))
    print(n1+n2)
    print("Thanks")

def ask_number():
    while True:
        try:
            number = int(input("Introduce a number: "))
        except:
            print("That is not a number")
        else:
            print(f"Your number is {number}")
            break
"""try:
    # the code we want to test
    
except:
    # the code to execute if the test fail
    
else:
    # the code to be executed if the test goes well
    
finally:
    # the code to be executed always
"""

ask_number()

try:
    addition()
except TypeError:
    print("Error: Different types")
except ValueError:
    print("Error: Not a number")
else:
    print("You did everything right ;)")
finally:
    print("Thats all folks!")