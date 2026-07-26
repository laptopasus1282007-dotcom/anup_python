status = input("Enter your marital status 'single' or 'married' :  ")

if status=="single" :
    gender = input("Enter your Gender 'male or 'female' : ")
    if gender=="male" :
        age = int(input("Enter a age :  "))
        if age>=21 :
            print("your eligible for married")

        else : 
            print("your Not eligible for married")



    elif gender=="female" :
        age = int(input("Enter a age :  "))
        if age>=18 :
            print("your eligible for married")
        else :
             print("your Not eligible for married")


    else :
        print("Please enter a male or female ")


elif status=="married" :
    print("You are already Married ")

else :
    print("Please enter single or married")