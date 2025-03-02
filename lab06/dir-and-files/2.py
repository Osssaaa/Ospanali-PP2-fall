import os

path = input("Input path of file: ")
path = os.getcwd()
print(f"Existence: {os.access(path, os.F_OK)}")
print(f"Readability: {os.access(path, os.R_OK)}")
print(f"Writability: {os.access(path, os.W_OK)}")
print(f"Executablity: {os.access(path, os.X_OK)}")