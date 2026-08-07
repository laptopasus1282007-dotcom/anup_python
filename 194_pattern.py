'''
0 
1 1 
0 0 0 
1 1 1 1 
0 0 0 0 0 
'''
for n in range(1,6):
    for num in range(1,n+1):
        if n%2!=0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()