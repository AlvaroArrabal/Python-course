from pathlib import Path, PureWindowsPath
import os


directory = Path("C:/Users/arrab/Desktop/DIA 6/DIA 6_1")        # creates a path in windowa with / instead of \
file = directory / "test_2.txt"                                 # appends to path

windowsPath = PureWindowsPath(file)

print(windowsPath)

print(file.read_text())                                         # an alternative for open("txt") and .read()
print(file.name)                                                # return the name of the file with that path, no parentheses
print(file.suffix)                                              # termination
print(file.stem)                                                # return the name of the file without the termination

os.system("cls")                                                # clear the terminal 

if not file.exists():
    print("File not found")
else:
    print("Correct")

