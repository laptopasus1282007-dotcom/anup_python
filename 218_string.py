#write a program to reverse a string.
name=input("Enter a string : ")
print("String : ",name)
reverse=""
for n in name :
    reverse=n+reverse
print("string reverse : ",reverse)

'''
#2nd code
name=input("Enter a string : ")
print("String : ",name)
reverse=""
reverse=name[::-1]
print("String Reverse : ",reverse)'''