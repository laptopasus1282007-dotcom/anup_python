'''Write a program to convert a string uppercase.
anup --> ANUP
aditi --> ADITI
'''
#code 1 
'''
name=input("Enter a string  : ")
uppercase=""

for n in name:
    uppercase=uppercase + chr(ord(n)-32)
print("UPPER CASE : ",uppercase)'''

#code 2 

name=input("Enter a string  : ")
uppercase=name.upper()
print("UPPER CASE : ",uppercase)