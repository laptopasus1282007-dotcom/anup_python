#list object in python  
#agar multiple employe ka data store karna hai to bar bar definr nhi 
#kr sakte isliye for loop lagaya

class Employe :
    def setEmploye(self):
        self.name = input("\nEnter Your Name : ")
        self.id = input("Enter your Id : ")
        self.role = input("Enter Your Role : ")
        self.salery = input("Enter your Salery : ")

    def getDetails(self):
        print("<-- Employe Details --> ")
        print(f"name = {self.name}")
        print(f"id = {self.id}")
        print(f"role = {self.role}")
        print(f"salery = {self.salery}")
        print("-----------------")


employes = []
n = int(input("Enter a number of Employe : "))
for i in range(n):
    em= Employe()
    employes.append(em)

for obj in employes :
    obj.setEmploye()


for obj in employes :
    obj.getDetails()   
