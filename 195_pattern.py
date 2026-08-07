'''
0
0 1
1 0 1
0 1 0 1
0 1 0 1 0
'''
for n in range(1, 6):
    for num in range(1, n + 1):
        if n == 1:
            print("0", end=" ")
        elif (n + num) % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()