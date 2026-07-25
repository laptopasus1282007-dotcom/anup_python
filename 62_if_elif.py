"""Write a program to calculate the total salary based on the basic salary:
If BS is between 4000 and 6000 -> TA 40% and HRA 20%
If BS is between 6000 and 10000 -> TA 45% and HRA 20%
If BS is greater than 10000 -> TA 55% and HRA 5000"""

bs = float(input("Enter a Basic Salary: "))

if 4000 <= bs <= 6000:
    ta = bs * 0.40
    hra = bs * 0.20
elif 6000 < bs <= 10000:
    ta = bs * 0.45
    hra = bs * 0.20
elif bs > 10000:
    ta = bs * 0.55
    hra = 5000
else:
    print("Invalid Salary")
    exit()

total = bs + ta + hra
print("Basic Salary =", bs)
print("TA =", ta)
print("HRA =", hra)
print("Total Salary =", total)

