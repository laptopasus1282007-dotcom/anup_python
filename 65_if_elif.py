"""Write a program to take a 2-digit, 3-digit, or 4-digit number from the user,
print its reverse, and print the sum of its individual digits.
If the number is not 2, 3, or 4 digits, print: please enter 2 or 3 or 4 digit number."""

num = int(input("Enter a number: "))

if 10 <= num <= 99:
    reverse = int(str(num)[::-1])
    digit_sum = sum(int(d) for d in str(num))
    print("Reverse number:", reverse)
    print("Sum of digits:", digit_sum)
elif 100 <= num <= 999:
    reverse = int(str(num)[::-1])
    digit_sum = sum(int(d) for d in str(num))
    print("Reverse number:", reverse)
    print("Sum of digits:", digit_sum)
elif 1000 <= num <= 9999:
    reverse = int(str(num)[::-1])
    digit_sum = sum(int(d) for d in str(num))
    print("Reverse number:", reverse)
    print("Sum of digits:", digit_sum)
else:
    print("please enter 2 or 3 or 4 digit number")