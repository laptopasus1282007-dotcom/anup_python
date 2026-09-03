#Write a program to count how many negative numbers are present in an array.

# Write a program to count how many positive numbers are present in an array. 

negative_count=0
list=[]
length=int(input("Enter a length of array element : "))
for i in range(length):
    name=int(input("Enter a Array of Elements : "))
    list.append(name)
print("List Are : ",list)

print(" Total negative numbers are present in an array : ",end=" ")
for n in list:
    if n < 0 :
        negative_count=negative_count+1

print(negative_count,end=" ")   
