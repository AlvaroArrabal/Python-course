list = ["a","b","c"]

for i in list:
    number = list.index(i)  # remember that lists, arrays, etc... begins at 0
    print(f"Letter: {i} and his index is {number}")
print("---------------------------")
list = ["Alvaro","Henry","Marc","Petter", "Hello"]

for i in list:
    if i.startswith("H"):
        print(f"The name of {i} starts with H")
    else:
        print(f"The name of {i} doesnt star with H")
print("---------------------------")
numbers = [1,2,3,4,5]
res = 0
for number in numbers:
    res = res + number
    print(res)
print("---------------------------")
word = "Hello"

for i in word:
    print(i)
print("---------------------------")
for i in "Hello":
    print(i)

print("---------------------------")
List = [[1,2],[3,4],[5,6]]   # its a "matrix"

for i in List:
    for j in i:
        print(j)

print("---------------------------")
for i,j in List:
    print(i)
    print(j)

