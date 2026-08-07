'''
1 1 1 1 
1 1 1 1 
0 0 0 0 
0 0 0 0 
'''
for n in range(1,5):
    for num in range(1,5):
        if n>2:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()