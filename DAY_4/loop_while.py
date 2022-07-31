n = 5

while n>0:
    print(f"Number: {n}")
    n -=1                           # n = n-1
else: 
    print("No more numbers")

print("---------------------------")

answer = "s"

while answer == "s":
    answer = input("Continue? (s/n): ")
else:
    print("exit!")

print("---------------------------")

name = input("name: ")
print("With break:")
for i in name:
    if i == "r":
        break
    print(i)
    
print("With continue:")
for i in name:
    if i == "r":
        continue
    print(i)
