'''
A B C D E 
B B B B B 
A B C D E 
D D D D D 
A B C D E 
'''
for n in range(65,70):
    for num in range(65,70):
        if n%2!=0 :
            print(chr(num),end=" ")
        else:
            print(chr(n),end=" ")
    print()