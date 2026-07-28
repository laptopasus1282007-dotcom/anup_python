"""Write a program that takes a number and a single digit as input, and counts
how many times the digit appears in the given number."""

number = input("Enter a number: ")
digit = input("Enter a single digit: ")

if len(digit) != 1 or not digit.isdigit():
    print("Please enter a single digit.")
else:
    count = 0
    i = 0

    while i < len(number):
        if number[i] == digit:
            count += 1
        i += 1

    print(f"The digit {digit} appears {count} times in the number {number}.")
