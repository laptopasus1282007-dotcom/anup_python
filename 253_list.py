#Write a program to display all negative numbers present in an array.

list=[]
length=int(input("Enter a length of array element : "))
for i in range(length):
    number=int(input("Enter a Array Element : "))
    list.append(number)
print("List is : ",list)

print("Display all negative numbers present in an array : ",end=" ")
for n in list:
    if n<0:
        print(n,end=" ")