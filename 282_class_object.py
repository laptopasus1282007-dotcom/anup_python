class mobile():
    def anup(self,company,colour,rating,price):
        self.company = company
        self.colour = colour  
        self.rating = rating
        self.price = price
        

    def getMobile(object):
        print("Mouse Info : ")
        print("company :",object.company)
        print("colour :",object.colour)
        print("rating :",object.rating)
        print("price :",object.price)
        print("---------------------")
        
m1=mobile()
m1.anup("Mototola","green","9.8","24999")
m1.getMobile()

m2=mobile()
m2.anup("Vivo","black","8.5","14999")
m2.getMobile()


