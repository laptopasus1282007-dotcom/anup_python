# Write a program to find sum of all number between 1-25 and check sum is 
# even or odd.

res = 0
for num in range(1,26):
    res=res+num

print(f"Sum of numbers from 1 to 25 is {res}.")
if res % 2 == 0:
    print("The sum is even.")
else:
    print("The sum is odd.")
