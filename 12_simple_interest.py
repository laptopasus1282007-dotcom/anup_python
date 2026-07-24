#write a program to calculate simple interest.
principle = eval(input("Enter the principle amount : "))
rate = eval(input("Enter the rate of interest : "))
time = eval(input("Enter the time in years : "))

interest = principle * rate * time / 100
print("simple interest : ",interest)

