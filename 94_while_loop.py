#Write a program to display number cube 1 to n (anup number)

anup=int(input("Enter your number : "))
num=1
while num<=anup:
    print(num*num*num,end=" ")
    num=num+1