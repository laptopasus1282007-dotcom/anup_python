#Write a program to print word according to number like 1 One 2 Two  upto 10.
num = int(input("Enter a number : "))
match num :
    case 1 :
        print("one")
    case 2 :
        print("two")
    case 3 :
         print("three")
    case 4 :
         print("four")
    case 5 :
        print("five")
    case 6 :
        print("six") 
    case 7 :
        print("seven")
    case 8 :
        print("Eight")
    case 9 :
        print("nine")
    case 10 :
        print("Ten")
    case _ :
        print("Enter a number 1 to 10 ")
    