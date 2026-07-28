""" Write a program to that takes a number as input and calculates the sum of 
only its even digits."""


num = int(input("Enter a number : "))#3242
ans=0
while num>0:
    rem=num%10
    if num%2==0:
        ans=ans+rem
    num=num//10
print("sum  of only even digits : ",ans)
