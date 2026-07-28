#Write a program to display factors of given number.
anup = int(input("Enter a number : "))
num = 1
print(f"Factor of {anup} : ",end=" ")
while num<=anup:
    if anup%num==0:
        print(num,end=" ")
    num+=1