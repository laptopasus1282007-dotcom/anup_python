"""Write a program to make simple calculator. 
      Press 1 to addition 
      Press 2 to subtraction 
      Press 3 to multiplication 
      Press 4 to division"""
print("<-------Welcome to My Calculator------->")
print("        Press 1 to addition ")
print("        Press 2 to subtraction ")
print("        Press 3 to multiplication ")
print("        Press 4 to division ")

num = int(input("Enter a number :  "))
match num:
    case 1:
        print("---<Addition Calculator--->")
        a=int(input("Enter value of a : "))
        b=int(input("Enter value of b : "))
        c=a+b
        print("Answer is : ",c)

    case 2:
        print("---<subtraction Calculator--->")
        a=int(input("Enter value of a : "))
        b=int(input("Enter value of b : "))
        c=a-b
        print("Answer is : ",c)

    case 3:
         print("---<Multiplication Calculator--->")
         a=int(input("Enter value of a : "))
         b=int(input("Enter value of b : "))
         c=a*b
         print("Answer is : ",c)

    case 4:
        print("---<division Calculator--->")
        a=int(input("Enter value of a : "))
        b=int(input("Enter value of b : "))
        c=a/b
        print("Answer is : ",c)

    case _:
        print("please Enter a 1 to 4 ")