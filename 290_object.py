class Real:
    def setHuman(self):
        self.name = input("\nEnter A Name : ")
        self.age= input("Enter A Age : ")
        self.village = input("Enter A Village Name : ")
        self.occation = input("Enter A Occation : ")

    def getHumandetails(self):
        print("--< Bike Details <--")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"village : {self.village}")
        print(f"occation : {self.occation}")
        print("---*---*---*---*---*---*")

human = []
n = int(input("Enter A Number Of Real : "))
for i in range(n):
    hu = Real()
    human.append(hu)

for obj in human :
    obj.setHuman()

for obj in human :
    obj.getHumandetails()