myList = ["a","b","c"] # Lists can have differents types of variables

result = len(myList) # return the legth of the list
print(result)

result = myList[0] # It return the data in that index of the list
print(result)

result = myList[0:2] # It return the data in that range of the list
print(result)

myList2 = ["d", "e","f"]
print(myList + myList2) # we can concatenate lists

myList3 = myList + myList2
print(myList3[0:]) # show all the content of the list

myList3[0] = "alfa"
print(myList3[0:])

myList3.append("g") # it appends another element to the list
print(myList3)

myList3.pop() # if you dont put an argument in the function, it deletes the last element in the list
print(myList3)

myList3.pop(0) # now, it deletes the element in index 0
print(myList3)

eliminated = myList3.pop(0) # we put the deleted element in a new variable
print(eliminated)

myList4 = ["g","o","b","m","c"]

myList4.sort()  # rearrange from largest to smallest. Important: the function doesnt return anything, its a nontype
print(myList4)

myList4.reverse() # rearrange from smallest to longest.
print(myList4)
