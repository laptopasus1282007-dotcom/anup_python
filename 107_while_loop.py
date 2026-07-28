""" Write a program takes a number as input and prints each digit of the 
number in reverse order, with each digit displayed on a separate line. """

num = int(input("Enter a number : "))
while num>0:
    rem=num%10
    print(rem)
    num=num//10 
