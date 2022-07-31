def check(List):
    for n in List:
        if n in range(100,1000):
            return True
        else:
            pass

List = [45,12,345]
res = check(List)

print(res)