#  Write a program to check given number is prime or not. 

given = int(input("Enter a number : "))
res = 0
for num in range(1,given+1):
     if given % num ==0 :
          res=res+1
if res==2:
     print("Number is Prime ")
else :
     print("Number is Not Prime ")
