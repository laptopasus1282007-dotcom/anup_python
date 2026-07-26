#Write a program to find greatest number among has given three numbers. 
#without using (and ,or) this type logical operator.

a = int(input("Enter a value of a --> "))
b = int(input("Enter a value of b --> "))
c = int(input("Enter a value of c --> "))

if a > b  :
    if a > c :
        print("Greatest Number is a : ",a)
    else : 
        print("Gretest number is c : ",c)


else :
    if b > c :
        print("Greatest number is b : ",b)

    else :
        print("Gretest number is c : ",c)
        