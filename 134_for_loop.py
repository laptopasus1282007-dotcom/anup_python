# Write a program to display multiple of 7 between given range.

anup = int(input("Enter a starting range : "))
aditi = int(input("Enter a ending range :  "))

for num in range(anup,aditi+1):
    if num%7==0:
        print(num)