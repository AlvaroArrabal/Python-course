# Dictionaries dont have indexes 

dictionary = {"c1":"v1","c2":"v2"}

print(dictionary)

result = dictionary["c1"] 
print(result)

client = {"name":"Alvaro","surname":"Arrabal","age":23,"height":1.75}
result = client["height"]
print(result)

dic = {"a":55, "b":[1,"e",3], "c":{"d":1,"f":"hello"}} # a dictionary with different types of variables

print(dic["b"][1]) # it show the content like a matrix in c++

print(dic["c"]["f"])

dictionary["3"] = "22"
dictionary["c2"] = "23"

print(dictionary)

print(dic.keys()) # it shows the keys of the dictionary

print(dic.items()) # it shows all the content