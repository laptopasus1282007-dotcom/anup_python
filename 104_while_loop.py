# Write a program to display factors count of given number. 
anup = int(input("Enter a number : "))
num = 1
dada=0
print(f"Total Factor Count {anup} : ",end=" ")
while num<=anup:
    if anup%num==0:
        dada=dada+1
    num=num+1
print(dada)