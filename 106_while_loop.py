#Calculate power of a number without using pow(). 
no = int(input("Enter a number : "))
power = int(input("Enter a power : "))
res = 1
num = 1
while num <= power:
    res = res * no
    num = num + 1
print(res)     
