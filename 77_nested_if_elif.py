#check a if number is even- positive , even - negative ,odd - negative or zero .
num = int(input("Enter a number : "))
if num % 2 ==0 :
    if num>=0 :
        print("even- positive")

    else :
        print("even - negative")

else : 
    if num>=0 :
        print("odd - positive")

    else :
        print("odd - negative")