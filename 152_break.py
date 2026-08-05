
n = [12, 3, 21, 20, 31, 56, 98, 14, 75, 77, 59, 73, 81, 93]
num = int(input("Enter a number : "))

for data in n:
    if num == data:
        print("Number is Found")
        break
else:
    print("Number is not Found")