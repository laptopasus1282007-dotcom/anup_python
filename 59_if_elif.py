"""Write a program to Check whether a person is a child, teenager, adult, or senior 
based on age."""

age = int(input("Enter a age : "))
if age >= 0 and age <= 13 :
    print("Child")

elif age >= 14 and age <= 18 :
    print("Teenager")

elif age >= 19 and age <= 60 :
    print("Adult")

elif age >= 61 and age <=100 :
    print("Senior")

else :
    print("Please Enter a vaild age ")
