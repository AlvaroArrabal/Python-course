from collections import Counter
from collections import defaultdict
from collections import namedtuple

# COUNTER
numbers=[2,4,7,2,5,8,3,6,8,3,5,8,3,8,5,9]

print(Counter(numbers))                             # Creates a dictionary with each number and the number of times it is repeated

print(Counter("mississippi"))

serie = Counter([1,1,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,4])

print(serie.most_common())
print(serie.most_common(1))                         # only shows the most common


#DEFAULTDICT

dic = defaultdict(lambda: "nothing")                # if the element is not in the dictionary, returns this
#dic = {"one":"green","two":"blue","three":"red"}
dic["one"] = "green"

print(dic["four"])
print(dic)                                          # defaultdict creates a new value for a search that has failed

#NAMEDTUPLE

Person = namedtuple("Person",["name","height","weight"])

carl = Person("Carl",1.76,78)

print(carl.height)
print(carl[1])