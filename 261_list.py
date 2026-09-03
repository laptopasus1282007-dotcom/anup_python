# Write a program to count how many elements in an array are multiples of 3.


count=0
list=[]
length=int(input("Enter a length of array element : "))
for i in range(length):
    number= int(input("Enter a array element : "))
    list.append(number)
print("List is : ",list)

print("Total count elements in an array are divisible by 3 : ",end=" ")
for n in list:
    if n%3==0:
        count=count+1
print(count,end=" ")