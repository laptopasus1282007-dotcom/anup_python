# Write a program to display all elements in an array that are multiples of 3. 

list=[]
length=int(input("Enter a length  : "))
for i in range(length):
    number= int(input("Enter a Array element : "))
    list.append(number)
print("List is : ",list)

print("display all elements in an array that are multiples of 3 : ", end=" ")
for n in list:
    if n%3==0 : 
        print(n,end=" ")



