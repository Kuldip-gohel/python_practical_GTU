A = input("Enter any character:")
vowel = "aeiouAEIOU"

for i in A:
    if i in vowel:
        print(i)

a = input("Enter 1 char:")
if (a=="a" or a=="e" or a=="i" or a=="o" or a=="u"):
    print("It is vowel")
else:
    print("it is consonent")
