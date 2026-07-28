''' Write a program to takes a number as input and calculates the sum of its 
individual digits.'''

num = int(input("Enter a number : "))
ans=0
while num>0:
    rem=num%10
    ans = ans+rem
    print(rem)
    num=num//10 
print("sum of individual digits : ",ans)