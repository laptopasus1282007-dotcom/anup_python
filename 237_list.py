# Write a programto take input and print all element of list
list=[]
given=int(input("Enter a list length : "))
for i in range(given):
    anup=int(input("Enter a List Element : "))    
    list.append(anup)

print("List Element are : ")
for n in list:
    print(n)