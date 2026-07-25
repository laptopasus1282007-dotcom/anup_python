"""Determine the grade based on marks. 
Marks (90-100) A grade 
Marks (75-89)  B grade 
Marks (50-74)  C grade 
Marks ( < 50)  F grade"""

marks = int(input("Enter a Marks : "))

if marks >= 90 and marks <= 100:
    print("A grade")

elif marks >=75 and marks <=89 :
    print("B grade")

elif marks >=50 and marks <= 74 :
    print("C grade")

else : 
    print("F garde")
