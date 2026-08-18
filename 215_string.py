#write a program to count the number of vovel and consonant 
#in a string.

name=input("Enter a name : ")
v=0
c=0
for n in name:
    if n in "aeiou":
        v=v+1
    else:
        c=c+1
print("number of vovel : ",v)
print("number of consonant : ",c)