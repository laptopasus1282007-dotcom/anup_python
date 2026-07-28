# Write a program to check given number is prime or not.

anup = int(input("Enter a number : "))
num = 1
dada=0
print(f"Total Factor Count {anup} : ",end=" ")
while num<=anup:
    if anup%num==0:
        dada=dada+1
    num=num+1

if dada==2:
    print("Number is prime")
else :
    print("Number is Not prime")