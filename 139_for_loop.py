# Write a program to display sum 1 to n  ( given number) 
# only multiple of 5 numbers sum. 

given = int(input("Enter a number : "))
res = 0
for num in range(1,given+1):
    if num%5==0:
        res=res+num
print(res)