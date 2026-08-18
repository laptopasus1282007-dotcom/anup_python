#wap to count only even number of digit in given number.

num=int(input("Enter a number : "))
num=str(num)
c=0
for n in num:
    if int(n)%2==0:
        c=c+1

print("Even Digit Count : ",c)