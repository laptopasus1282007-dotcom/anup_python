#Write a program to display sum 1 to n ( given number). 
anup = int(input("Enter a number : ")) #13
num=1
res=0
while num<=anup: 
    res=res+num #1 3 6 10 15 21 28 36 45 55 66 78 91 
    num=num+1
    print(res)