"""
0 0 0 0 
1 1 1 1 
0 0 0 0 
1 1 1 1 
"""
for n in range(1,5):
    for num in range(1,5):
        if n%2==0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()