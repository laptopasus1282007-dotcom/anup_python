#Write a program to input and print all elements of an array.

list=[]
n=int(input("Enter a list length : "))
for i in range(n):
    num=int(input("Enter a List Element :"))
    list.append(num)
  
print("List Elemennt Are : ")
for element in list:
    print(element)