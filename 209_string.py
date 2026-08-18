#wap to check how manny vovel in string.
string=input("Enter a string : ")
v=0
c=0
for ch in string:
    if ch in "aeiou":
        v=v+1
    else:
        c=c+1
print("string is : ",string )
print("total vovel in string : ",v)
print("total conconesnt in string : ",c)