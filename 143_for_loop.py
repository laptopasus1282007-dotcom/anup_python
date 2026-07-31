# Write a program to display factors of given number. 

given = int(input("Enter a number : "))
for num in range(1, given + 1):
    if given % num == 0:
        print(num)
