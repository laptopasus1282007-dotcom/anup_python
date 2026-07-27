# Write a program to display even number series.
anup =int(input("Enter a number : "))
num=1
while num<=anup:
    if num%2==0:
        print(num,end=" ")
    num=num+1