List = ["a", "b", "c", "d"]


for i in enumerate(List):
    print(i)

print("-------")

for index,i in enumerate(List):
    print(index,i)

print("-------")

myTupple = list(enumerate(List))
print(myTupple)