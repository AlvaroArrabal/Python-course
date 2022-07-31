import os

myPath = os.getcwd()                                                        # actual path
print(myPath)

myPath = os.chdir("C:\\Users\\arrab\\Desktop\\DIA 6\\DIA 6_1")              # Change directory

text = open("test_2.txt")                                                   # Open a file in the new directory
print(text.read())

myPath = os.makedirs("C:\\Users\\arrab\\Desktop\\DIA 6\\DIA 6_1\\DIA 6_2")  # Create a new directory, if the directory already exists it gives an error

os.rmdir("C:\\Users\\arrab\\Desktop\\DIA 6\\DIA 6_1\\DIA 6_2")              # removes the directory

myPath = "C:\\Users\\arrab\\Desktop\\DIA 6\\DIA 6_1\\test_2.txt"

element = os.path.basename(myPath)                                          # return the name of the file in the path
print(element)

element = os.path.dirname(myPath)                                           # return the name of the directory
print(element)

element = os.path.split(myPath)                                             # return a tuple with the directory and the name of the file
print(element)

