#Write a program to display even number series. 

given = int(input("Enter a number : "))
for  num in range(1,given+1):
    if num%2==0:
        print(num)