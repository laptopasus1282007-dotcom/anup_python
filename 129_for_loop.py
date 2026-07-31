# Write a program to display number cube 1 to n (given number).

given = int(input("Enter a num : "))
for num in range(1,given+1):
    print(f"cube of {num} : {num*num*num}")