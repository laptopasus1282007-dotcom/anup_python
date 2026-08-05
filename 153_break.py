
given = int(input("Enter a number 1 to 10 : "))
for num in range(1,11):
    if num==given:
        print("Break is Exicute")
        break

    print(num)
else:
    print("Else is Exicute")