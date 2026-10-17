#jo bhi display karna hai woh user se lenge

class Employe :
    def setEmploye(self):
        self.name = input("Enter Your Name : ")
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


s1 = Employe()
s1.setEmploye()
s1.getDetails()

s2 = Employe()
s2.setEmploye()
s2.getDetails()
