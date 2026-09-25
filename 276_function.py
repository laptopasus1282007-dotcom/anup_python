#function With Parameter.

def add (a,b) :   #here 2 parameter a and b.
    c=a+b
    print("addtion is : ",c)


def square (num) :
    res = num * num 
    print(f"Sqaure of {num} = {res}")


def greater (num1,num2) :
    if num1 > num2 :
        print("greater num = ",num1)
    else :
        print("greater num = ",num2)

def table (num) :
    for i in range(1,11):
        print(f"{num} x {i} = {num * i }")


    #main Program


add(12,5)
add(7,5)
add(2,1)
add(15,7)

print("-------------------")


square(12)
square(7)
square(5)
square(20)


print("-------------------")


greater(12,21)
greater(12,3)
greater(55,54)
greater(7,3)

print("-------------------")


table(12)
table(3)
table(21)





