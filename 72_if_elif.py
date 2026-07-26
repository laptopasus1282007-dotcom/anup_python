""" Write a  program to check whether a character is uppercase alphabet or lowercase 
alphabet or not alphabet."""

char = input("Enter a alphabbet : ")

if  char >= 'a' and char <= 'z' :
    print("Charcter is Lowercase Alphabet ")

elif char >= 'A' and char <= 'Z' :
    print('Charcter is Uppercase Alphabet')

else :
    print("This is not Alphabet")
