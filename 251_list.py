#Write a program to display all odd numbers present in an array. 

list=[]
length=int(input("Enter a length of array element : "))
for i in range(length):
    number=int(input("Enter a array element : "))
    list.append(number)
print("List is : ",list)

print("Display only odd numbers present in an array : ",end=" ")
for n in list:
    if n%2!=0:
        print(n,end=" ")