mySet = set([1,2,3,4,5]) # sets only admits 1 argument
print(mySet)

mySet2 = {1,2,3} # its also a set
print(type(mySet2)) 
print(mySet2)


mySet = set([1,2,3,4,5,1,1,2,2,2,3,3,3,2,2,1,1,1,7]) # unique elements
print(mySet)

# you can introduce tuples in sets. but you can't introduce dictionaries or lists

mySet3 = mySet.union(mySet2)
print(mySet3)

mySet3.remove(7)  # instead of remove we can use discard, the difference is that discard dont stop if you put an argument that is not in the set
print(mySet3)

# the function .pop delete an aleatory element
# .clear delete all data
# .add add a element to set