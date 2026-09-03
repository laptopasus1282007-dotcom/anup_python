# Write a program to count how many elements in an array are divisible by 4.
count=0
list=[]
length=int(input("Enter a length of array element : "))
for i in range(length):
    number= int(input("Enter a array element : "))
    list.append(number)
print("List is : ",list)

print("Total count elements in an array are divisible by 4 : ",end=" ")
for n in list:
    if n%4==0:
        count=count+1
print(count,end=" ")