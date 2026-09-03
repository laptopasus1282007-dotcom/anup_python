#Write a program to print squares of all numbers present in a given array.

list=[]
length=int(input("Enter a length of array element : "))
for i in range(length):
    name=int(input("Enter a Array of Elements : "))
    list.append(name)
print("List is : ",list)

print("Sqaure of all array elements : ",end=" ")
for n in list:
    print(n*n,end=" ")