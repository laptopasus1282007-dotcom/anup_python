""" Write a program to check whether a character is an alphabet, digit or special 
character."""
char = input("Enter a charcter : ")
if char>='a' and char<='b' or char>='A' and char<='Z':
    print("charcter is alphabet")
elif char>='0'and char<='9':
    print("charcter is digit")
else :
    print("special symbol")