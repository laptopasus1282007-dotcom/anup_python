# Write a program to display number square 1 to n (given number).

given = int(input("Enter a number : "))
for num in range(1,given+1):
    print(f"square of {num} : {num*num}")