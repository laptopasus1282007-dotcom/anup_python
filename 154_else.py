#wap to check number prime or not.

given =int(input("Enter a number : "))
for num in range(2,given):
    if given%num==0:
        print("Number is not prime")
        break
else:
    print("Number is prime")