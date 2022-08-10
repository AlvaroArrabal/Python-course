import timeit
# "timeit" for small processes

declaration = """
test_for(10)
"""

mySetUp = """
def test_for(num):
    myList = []
    for i in range(1,num+1):
        myList.append(i)
    
    return myList
"""

duration = timeit.timeit(declaration,mySetUp,number = 100000)

print(f"for: {duration}")

declaration2 = """
test_while(10)"""

mySetUp2 = """
def test_while(num):
    myList = []
    i = 1
    while i <= num:
        myList.append(i)
        i +=1
    
    return myList
"""

duration2 = timeit.timeit(declaration2,mySetUp2,number = 100000)

print(f"while: {duration2}")