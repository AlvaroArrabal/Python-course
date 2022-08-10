import time

def test_for(num):
    myList = []
    for i in range(1,num+1):
        myList.append(i)
    
    return myList

def test_while(num):
    myList = []
    i = 1
    while i <= num:
        myList.append(i)
        i +=1
    
    return myList

begin = time.time()                     # "time.time()"" is for large processes
test_for(100000)
end = time.time()
print(f"test for {end-begin}")

begin = time.time()
test_while(100000)
end = time.time()
print(f"test while {end-begin}")
