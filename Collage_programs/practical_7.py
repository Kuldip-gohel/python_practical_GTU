# Write a python program to generate empty list  
empty = []

# perform insertion of elements in it using append(). extend() and insert()
empty.append(["apple","mango"])
empty.extend(["lichi"])
empty.insert(1,"graps")
print(empty)

# print length of list. value of element located at index 2
print(len(empty))
print((empty[2]))

# occurrences of element located at index 2  

# print reverse list
print(empty[::-1])

# Check whether specific value is available in list using membership operator

# Deletion of elements using pop(). remove() and clear() methods.
empty.pop()
print(empty)
empty.remove("graps")
print(empty)
empty.clear()
print(empty)