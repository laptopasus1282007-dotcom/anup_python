# Write a program to display average 1 to n ( given number).    

given = int(input("Enter a number : "))#
res = 0

for num in range(1, given + 1): 
    res = res + num

average = res / given
print("Average from 1 to", given, "is", average)