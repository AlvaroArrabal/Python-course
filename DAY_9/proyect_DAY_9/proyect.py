import os
import re
import datetime
import time
from pathlib import Path

path = "C:\\Users\\arrab\\Desktop\\PYTHON_COURSE\\DAY_9\\proyect_DAY_8\\Mi_Gran_Directorio"

myPattern = r"N\D{3}-\d{5}"
d = datetime.date.today()
cont = 0
print("--------------------------------------")
print(f"date: {d}")
print("FILE             Number")
print("----             ------")
begin = time.time()
for folder,subfolder,file in os.walk(path):
      
    for f in file:
        nameFolder = open(Path(folder,f),"r")
        text = nameFolder.read()
        check = re.search(myPattern,text)
        if check :
            cont += 1
            print(f"{f}     {check.group()}")
        nameFolder.close()

end = time.time()
print(f"\nFiles found: {cont}")
print(f"Search duration: {end - begin}")
print("--------------------------------------")