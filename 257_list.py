# Write a program to count how many odd numbers are present in an array.
odd_count=0
list=[]
length=int(input("Enter a length of array element : "))
for i in range(length):
    name=int(input("Enter a Array of Elements : "))
    list.append(name)
print("List Are : ",list)

print("Total odd number count :  ",end=" ")
for n in list:
    if n % 2 != 0 :
        odd_count=odd_count+1

print(odd_count,end=" ")
