#Write a program to find greatest number among has given four numbers. 
#without using (and ,or) this type logical operator
a = int(input("Enter a value of a --> "))
b = int(input("Enter a value of b --> "))
c = int(input("Enter a value of c --> "))
d = int(input("Enter a value of d --> "))


if a>b :
    if a>c :
        if a>d :
            print("Greatest Number is a : ",a)
        else :
            print("Greatest Number is d : ",d)
    else :
        if c>d :
            print("Greatest Number is c : ",c)
        else :
            print("Greatest Number is d : ",d)

else :
    if b>c:
        if b>d :
         print("Greatest Number is b : ",b)
        else :
         print("Greatest Number is d : ",d)

    else :
       if c>d:
          print("Greatest Number is c : ",c)
       else :
          print("Greatest Number is d : ",d)



   