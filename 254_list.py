# Write a program to display all elements in an array that are divisible by 4.

list=[]
length=int(input("Enter a length of array element : "))
for i in range(length):
    number= int(input("Enter a array element : "))
    list.append(number)
print("List is : ",list)

print("Display all elements in an array that are divisible by 4",end=" ")
for n in list:
    if n%4==0:
        print(n,end=" ")

