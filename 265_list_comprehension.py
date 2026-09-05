#list comprehension : List comprehennsion offers the shortest 
# syntax for looping through lists.
#its mostly used to make a new list with existing list.

#wap to make a new list which containe sqaure of 
# given list.

"""list1=[12,8,3,10,21,8]
list2=[]
for i in list1:
    square= i * i 
    list2.append(square)

print("Input List : ",list1)
print("Sqaure List : ",list2)"""


'''Same Question by using list comprehension'''

list1=[12,8,3,10,21,8]
list2=[i*i for i in list1]
print("Input List : ",list1)
print("Sqaure List : ",list2)

