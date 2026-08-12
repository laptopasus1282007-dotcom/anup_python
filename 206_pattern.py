"""
        * 
      * * 
    * * * 
  * * * * 
* * * * *  
"""
for n in range(1,6):
    for space in range(5,n,-1):
        print(" ",end=" ")
    for num in range(1,n+1):
        print("*",end=" ")
    print()