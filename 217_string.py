'''Write a program to convert a string uppercase.
anup --> ANUP
aditi --> ADITI
'''

name=input("Enter a string  : ")
uppercase=""

for n in name:
    uppercase=uppercase + chr(ord(n)-32)
print("UPPER CASE : ",uppercase)