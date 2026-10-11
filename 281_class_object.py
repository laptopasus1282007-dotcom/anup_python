class mouse():
    def aditi(self,company,colour,rating,price):
        self.company = company
        self.colour = colour  
        self.rating = rating
        self.price = price
        

    def getMouse(self):
        print("Mouse Info : ")
        print("company :",self.company)
        print("colour :",self.colour)
        print("rating :",self.rating)
        print("price :",self.price)
        print("---------------------")

        
m1=mouse()
m1.aditi("Zebronics","black","9.5","899")
m1.getMouse()

m2=mouse()
m2.aditi("HP","White","8.5","799")
m2.getMouse()


