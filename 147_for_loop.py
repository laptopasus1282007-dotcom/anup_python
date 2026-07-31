#Write a program to check given number is perfact or not. 

given = int(input("Enter a number : "))
res = 0
for num in range(1,given+1):
     if given % num ==0 :
          res=res+num

if res == num*2:
    print("number is perfact")
else : 
     print("number is not perfact")