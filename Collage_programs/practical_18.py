# Write a python program to print the length of each line

with open ("p18.txt","r") as file:
    for line in file:
        print(len(line))
