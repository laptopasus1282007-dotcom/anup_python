""" Write a program that takes a number as input and counts how many odd 
digits it contains."""

num=int(input("Enter a number : "))
ans = 0
while num>0:
    rem=num%10
    if rem%2!=0:
     ans=ans+1 
    num=num//10
print("odd digit count in number : " ,ans)