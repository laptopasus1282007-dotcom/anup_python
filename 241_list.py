#list.remove() :- list element delete in list.

list=[10,20,30,40,50,"anup"]
print(list)

print("****************************")

list.remove(10)
print(list)

print("****************************")

list.remove(20)
list.remove(40)
list.remove(30)
print(list)

print("****************************")

list.remove(50)
list.remove("anup")
print(list)