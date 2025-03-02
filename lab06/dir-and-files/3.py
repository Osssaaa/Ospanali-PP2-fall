import os
path = input("Input path of file: ")
if os.path.exists(path):
    print("File name:", os.path.basename(path))
    print("Directory:", os.path.dirname(path))
else:
    print("don't exists")