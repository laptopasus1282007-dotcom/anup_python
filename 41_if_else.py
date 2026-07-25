#Write a program to check given number is divisible by 3, 4 and 8 or not.
num = int(input("Enter a number : "))
if num % 3 == 0 and num % 4 == 0 and num % 8 == 0 :
    print("Number is divisible by 3, 4 and 8 ")
else :
    print("number is Not divisible by 3, 4 and 8")
    
