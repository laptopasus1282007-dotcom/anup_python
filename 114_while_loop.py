"""Write a program that takes a number and a single digit as input, and checks
whether the digit exists in the given number or not."""

number = input("Enter a number: ")
digit = input("Enter a single digit: ")

if len(digit) != 1 or not digit.isdigit():
    print("Please enter a single digit.")
else:
    i = 0
    found = False

    while i < len(number):
        if number[i] == digit:
            found = True
            break
        i += 1

    if found:
        print(f"Digit {digit} exists in the number {number}.")
    else:
        print(f"Digit {digit} does not exist in the number {number}.")