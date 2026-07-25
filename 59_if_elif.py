"""Write a program to Check whether a person is a child, teenager, adult, or senior 
based on age."""

age = int(input("Enter a age : "))
if age <= 14 :
    print("Child")

elif age <= 18 :
    print("Teenager")

elif age <= 60 :
    print("Adult")

else :
    print("Senior")
