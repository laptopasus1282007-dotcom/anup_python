#Write a program to print name of day according to number.
# #match case method.
day = int(input("Enter a number : "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wendsday")
    case 4 :
        print("Thusday")
    case 5 : 
        print("Friday")
    case 6 : 
        print("Saturday")
    case 7 : 
        print("Sunday")
    case _ :
        print("Enter a number 1 to 7")