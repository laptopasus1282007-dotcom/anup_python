#. Calculate power of a number without using pow(). 
anup = int(input("Enter a number : "))
aditi = int(input("Enter a power : "))
res=1
for n in range(aditi):
    res=res*anup
print(res)