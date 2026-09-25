#for loop in function

def add():
    a=int(input("Enter a : "))
    b=int(input("Enter b : "))
    c=a+b
    print("Addition Is : " ,c)

def sub():
    a=int(input("Enter a : "))
    b=int(input("Enter b : "))
    c=a-b
    print("Substraction Is : ",c)

#main program :-

for i in range(5):
    add()
