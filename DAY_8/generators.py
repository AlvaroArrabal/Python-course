def my_function():
    x = 1
    yield x             # wait here until the program really needs it. Better for memory

    x += 1
    yield x

    x+=1
    yield x

a = my_function()

print(next(a))          # with "next()" we inform to "yield" that we now need the variable in memory
print(next(a))
print(next(a))