"""Write a program to read the age of a candidate a determine whether the 
eligible to cast his/her own vote india or not"""

region = input("Enter your Region : ")

if region=='india':
    age = int(input("Enter your Age : "))

    if age >= 18 :
        print("You can Eligible for vote in india")
    else :
        print("you are not eligible")

else :
    print("You are not Indian ")        