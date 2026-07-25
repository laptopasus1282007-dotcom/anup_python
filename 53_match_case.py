"""Write a program using match-case that takes the first letter of a country 
name as input and prints a full country name starting with that letter."""

name = input("Enter a country short name : ")

match name :
    case "ind":
        print("INDIA")
    case "pak" :
        print("BHIKARISTAN")
    case "wl":
        print('WEST-INDIES')
    case "aus" :
        print("Austrila")
    case "afg" :
        print("AFGANISTAN")
    case "nz":
        print("NEWZLEND")
    case _:
        ("Enter a valid short name ")