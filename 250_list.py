#Write a program to display all even numbers present in an array.

list=[]
length=int(input("Enter a length of array elemennt : "))
for i in range(length):
    number=int(input("Enter a number of element : "))
    list.append(number)

print("list is : ",list)
print("display only even numbers present in an array : ",end=" ")
for n in list:
    if n%2==0:
        print(n,end=",")