# Write a program to display factors count of given number. 

given = int(input("Enter a number : "))
res=0
for num in range(1,given+1):
    if given % num ==0:
        res=res+1
print(res)