#mini clube entry project.

age = int(input("Enter a age : "))

if age >= 18 :
    print(" <--- Welcome to Clube ---> ")
    print("Clube Menu card")
    print("1. Pizza : 299")
    print("2. Momos : 99")
    print("3. Burger : 129")
    print("4. cold coffe : 70")
    print("5. Cold Drink : 50")
    order = int(input("Enter your order Number : "))

    if  order==1 :
        print("Your Pizza is Ordered please pay a 299rs")

    elif  order==2 :
        print("Your Momos is Ordered please pay a 99rs")

    elif  order==3 :
        print("Your Burger is Ordered please pay a 129")

    elif  order==4 :
        print("Your cold coffe is Ordered please pay a 70rs")

    elif  order==5 :
         print("Your coid drink is Ordered please pay a 50rs")

    else :
        print("Please enter a 1,2,3,4 and 5")    

else :
    print('Your Entry is not allowed in clube')