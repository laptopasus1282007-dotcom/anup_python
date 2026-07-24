"""Write a program to accept a number and check it is multiple of 3,5,8 or multiple of 
3,5 or multiple of 5,8 or multiple of 3,8 or only multiple of 3 or only multiple of 5 or 
only multiple of 8  or not multiple of 3,5,8."""

num = int(input("Enter a number : "))

if num%3==0 and num%5==0 and num%8==0 :
    print("Multiply by 3,5,8")

elif num%3==0 and num%5==0 :
    print("Multiply by 3,5")

elif num%5==0 and num%8==0 : 
    print("Multiply by 5,8")

elif num%3==0 and num%8==0 :
    print("Multiply by 3,8")

elif num%3==0 :
    print("Multiply by 3")

elif num%5==0 :
    print("Multiply by 5")

elif num%8==0 :
    print("Multiply by 8")

else :
    print("")

