rno = int(input("Enter your roll no. : "))
s1 = int(input("Enter a marks Maths : "))
s2 = int(input("Enter a marks Data structure : "))
s3 = int(input("Enter a marks Constitution of india : "))
s4 = int(input("Enter a marks Human Values : "))
s5 = int(input("Enter a marks Operating System : "))

if s1>=40 and s2>=40 and s3>=40 and s4>=40 and s5>=40 :
    print("Student roll no. : ",rno)
    print("Student Pass in Exam")
    per = ((s1+s2+s3+s4+s5)/500)*100
    print("percentage : ",per)

    if per >= 75 and per <= 100 :
        print("Grade A")

    elif per >= 60 and per < 75 :
        print("Grade B")

    elif per >= 50 and per < 60 :
        print("Grade C")

    elif per >= 40 and per < 50 :
        print("Garde D")

else : 
    print("Student Fail in  Exam ")







