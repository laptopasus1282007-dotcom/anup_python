#Write a program to display the array elements in reverse order.

list=[]
length=int(input("Enter a length of array element : "))
for i in range(length):
    name=int(input("Enter a Array of Elements : "))
    list.append(name)
print("List are : ",list)

print("Reverse Array element is : ",list[::-1])