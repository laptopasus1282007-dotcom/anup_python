#Write a program to find greatest number among has given four numbers. 

a = int(input("Enter a value of a --> "))
b = int(input("Enter a value of b --> "))
c = int(input("Enter a value of c --> "))
d = int(input("Enter a value of d --> "))


if a > b and a > c and a > d :
    print("Greatest Number is a : ",a)

elif b > c and b > d :
    print("Greatest Number is b : ",b)

elif c > d :
    print("Greatest Number is c : ",c)

else : 
    print("Greatest Number is d : ",d)