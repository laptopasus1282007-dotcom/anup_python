#Write a program to find smallest number among has given three numbers. 
a = int(input("Enter a Value of a : "))
b = int(input("Enter a Value of b : "))
c = int(input("Enter a Value of c : "))

if a < b and a < c :
    print("Smallest Number is a : ",a)

elif b < c :
    print("Smallest number is b : ",b)

else :
    print("Smallest number is c : ",c)
 