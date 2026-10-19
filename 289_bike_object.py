class bike:
    def setBike(self):
        self.name = input("\nEnter A Bike Name : ")
        self.model = input("Enter A Model : ")
        self.colour = input("Enter A Bike Colour : ")
        self.price = input("Enter A Price : ")

    def getBikedetails(self):
        print("--< Bike Details <--")
        print(f"Name : {self.name}")
        print(f"Model : {self.model}")
        print(f"Colour : {self.colour}")
        print(f"Price : {self.price}")
        print("---*---*---*---*---*---*")

bikes = []
n = int(input("Enter A Number Of Bikes : "))
for i in range(n):
    bi = bike()
    bikes.append(bi)

for obj in bikes :
    obj.setBike()

for obj in bikes :
    obj.getBikedetails()