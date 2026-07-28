''' Write a program that takes a number as input and counts how many digits 
it contains.'''

num=int(input("Enter a number : "))
ans = 0
while num>0:
    ans=ans+1 
    num=num//10
print("total digit count in number : " ,ans)