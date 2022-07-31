names = ["Alvaro","John", "Jane"]
ages = [23,24,35,46]

myZip = list(zip(names,ages))       # it takes the shorter list, we can combinate more than 2 lists
print(myZip)


print("----------------------------------")
cities = ["Madrid", "London", "Rome"]

myZip2 = list(zip(names,ages,cities))   
print(myZip2)

print("----------------------------------")

for name,age,city in myZip2:
    print(f"{name} has {age} years old and is from {city}")

