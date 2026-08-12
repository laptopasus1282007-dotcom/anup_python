'''
  5 5 5 5 
   4 4 4 4 
    /03 3 3 
      2 2 
        1 
'''

for n in range(5,0,-1):
    for space in range(5,n,-1):
        print(" ",end=" ")
    for num in range(1,n+1):
        print(n,end=" ")
    print()