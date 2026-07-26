#Write a program to find greatest number among has given three numbers.

a = int(input("Enter a Value of a : "))
b = int(input("Enter a Value of b : "))
c = int(input("Enter a Value of c : "))

if a > b and a > c :
    print("Greatest Number is a : ",a)

elif b > c :
    print("Greatest number is b : ",b)

else :
    print("Greatest number is c : ",c)
 