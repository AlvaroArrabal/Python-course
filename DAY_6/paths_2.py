from importlib.resources import path
from pathlib import Path

currentPath = Path(Path.home(),"Desktop","DIA 6")       # home() return the path to home, and the other parameters are the path to directory

for i in Path(currentPath).glob("*.py"):                # glob, iterate only with the elements with *.py (or anything you put there)
    print(i)

