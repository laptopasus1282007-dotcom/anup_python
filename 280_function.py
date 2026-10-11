#lambda function :- its pprovide shortest syntext to write small function.

add = lambda  a,b : a+b 

multi = lambda a,b : a*b

sqaure = lambda num : num*num

Display = lambda : print("Hello I am Anup ")

Negpos = lambda num : "positive" if num>0 else "negative"

greater = lambda a,b : a if a > b else b

greater3 = lambda a,b,c : a if a>b and a>c else b if  b>c else c   

print(add(12,3))
print(multi(12,3))
print(sqaure(12))
Display()
print(Negpos(-2))
print(greater(3,21))
print(greater3(5,3,12))