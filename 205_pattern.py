"""
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
"""
for n in range(1,6):
    for space in range(1,n):
        print(" ",end=" ")
    for num in range(6,n,-1):
        print("*",end=" ")
    print() 