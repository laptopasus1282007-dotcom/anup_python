#print statement with a format method.
name = "anup wasankar"
age = 19 
height = 6.1 
a= 12
b= 3
c = a+b
print ("my name is {}".format(name))
print ("my age is {}".format(age))
print ("my height is {}".format(height))
print ("sum of {} and {} = {}".format(a,b,c))

print ("sum of {2} and {1} = {0}".format(a,b,c)) #a=0 b=1 c=2

print ("sum of {y} and {y} = {y}".format(x=a,y=b,z=c)) #x=a y=b z=c
