#Write a program to input and print all students name  in list element.69
student=[]
n= int(input("Enter a length of list : "))
for i in range(n):
    name=input("Enter a Students Name : ")
    student.append(name)

print("List Students name are : ")
for std in student:
    print(std)