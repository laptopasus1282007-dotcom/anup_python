"""Write a program to check whether a string is a palindrome or not.
Ex -- > naman 
        madam 
"""

name=input("Enter a string : ")
print("string : ",name)
reverse=""

for n in name: 
    reverse=n+reverse
if name==reverse:
    print("string is palindrome")
else:
    print("string is not palindrome")