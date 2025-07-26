import os
filename = input("Enter file name:")
path,ext = os.path.splitext(filename)
print("Extention is -->",ext)
print("file path is -->",path)
