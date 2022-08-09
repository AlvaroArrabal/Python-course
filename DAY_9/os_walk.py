import os


path = "C:\\Users\\arrab\\Desktop\\PYTHON_COURSE\\DAY_6"

for folder, subfolder, file in os.walk(path):
    print(f"in {folder}")
    print("subfolders: ")
    for sub in subfolder:
        print(f"\t{sub}")
    print("files: ")
    for f in file:
        print(f"\t{f}")
    print("\n")