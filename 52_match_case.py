"""Write a program using match-case to print your friend's name based on the 
first letter of their name."""
name = input("Enter a first letter your friend :  ")
match name :
    case "a":
        print("ANUP")
    case "v":
        print("VIVEK")
    case "ad" :
        print("ADITI")
    case "p":
        print("PALAK")
    case "j":
        print("JAYESH")
    case _:
        print("Enter a valid name ")