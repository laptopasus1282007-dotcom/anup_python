class student:
    def setStudent(self, name, rno, age, city, per):
        self.name = name
        self.rno = rno
        self.age = age
        self.city = city
        self.per = per

    def display(self):
        print("Student Info : ")
        print(f"name = {self.name}")
        print(f"rno = {self.rno}")
        print(f"age = {self.age}")
        print(f"city = {self.city}")
        print(f"per = {self.per}")
        print("-------------------")


s1 = student()
s1.setStudent("Anup", "122", "19", "Akola", "89.5")
s1.display()

s2 = student()
s2.setStudent("Aditi", "125", "19", "Warud", "93.5")
s2.display()
    