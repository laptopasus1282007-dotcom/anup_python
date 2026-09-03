# Write a program to count how many even numbers are present in an array. 
even_count=0
list=[]
length=int(input("Enter a length of array element : "))
for i in range(length):
    name=int(input("Enter a Array of Element : "))
    list.append(name)
print("List is : ",list)

print("Total Evan number count : ",end=" ")
for n in list:
    if n%2==0:
        even_count=even_count+1

print(even_count,end=" ")
