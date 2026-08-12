"""
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
"""
for n in range(1,6):
    for num in range(n,0,-1):
        if num%2!=0:
            print("1",end=" ")
        else :
            print("0",end=" ")
    print()