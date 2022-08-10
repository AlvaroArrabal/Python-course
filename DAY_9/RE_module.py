# RE = Regular Expressions
import re


text = "call 123-123-123"

myPattern = r'\d{3}-\d{3}-\d{3}'

res = re.search(myPattern,text)

print(res.group())


password = input("Password: ")
myPattern = r"\D{1}\w{7}"

check = re.search(myPattern,password)
print(check)



# \d digit
# \w alphanumeric character
# \s space
# \D not a digit
# \W not an alphanumeric character
# \S not a space

# Quantifiers
# + one or more time
# {n} n times
# {n,m} n to m times
# {n,} n time minimum
# * 0 or more time
# ? once or none


