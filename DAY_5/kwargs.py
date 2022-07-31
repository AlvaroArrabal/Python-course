def addition(**kwargs):          # **kwargs creates a dictionaty with de arguments
    total = 0

    for key,value in kwargs.items():
        print(f"{key} = {value}")
        total += value

    return total

print(addition(x=3, y=5, z=1))

def example(num1,num2,*args,**kwargs):
    print(f"The first value is {num1}")
    print(f"The second value is {num2}")

    for i in args:
        print(f"args = {i}")

    for key,value in kwargs.items():
        print(f"{key} = {value}")

example(2,3,4,5,6,7,8,9,10,x=5,y=1,z="three")