#How to add new value in destionary.

student={"Anup":122, "Aditi":125, "Palak":100,}
print(student)


#this method Add new element in destionary. 1st method
"""student["Bhushan"]=260
print(student)
"""

#using update  add new elememt in distionary. 2nd method
#Isme hum multiple value add kr sakte hai.
student.update({"vivek":50,"raj":20,"satish":31})
#student.update({"vivek":41})
print(student)