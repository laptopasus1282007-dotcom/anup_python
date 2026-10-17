#code No.283 aani ha same ahe fkt ya madhe percentage sathi if else cha use kela student
#  pass and fail show sathi.


class student:
    def setStudent(self, name, rno, age, city, per):
        self.name = name
        self.rno = rno
        self.age = age
        self.city = city
        self.per = float(per)

    def display(self):
        print("Student Info : ")
        print(f"name = {self.name}")
        print(f"rno = {self.rno}")
        print(f"age = {self.age}")
        print(f"city = {self.city}")

        if self.per >= 35:
            print("Student Pass")
        else:
            print("Student Fail")

        print("------------------")


s1 = student()
s1.setStudent("Anup", 122, 19, "Akola", 89.5)
s1.display()

s2 = student()
s2.setStudent("Aditi", 125, 19, "Warud", 93.5)
s2.display()

s3 = student()
s3.setStudent("Palak", 261, 19, "Chandrpur", 84.2)
s3.display()