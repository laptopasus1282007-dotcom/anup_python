#Write a program to find sum of array elements & check sum is even or odd.

list=[12,8,3,10,21,8]
print("List is : ",list)

sum=0
for num in list:
    sum=sum+num
print("Sum of array elements is : ",sum)
if sum%2==0:
    print("Sum is Even")
else:
    print("Sum is Odd")