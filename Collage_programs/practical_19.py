# Write a python program to print first 15 bytes from file using with open.

with open("p18.txt","r") as file:
    data = file.read(15)
    print(data)