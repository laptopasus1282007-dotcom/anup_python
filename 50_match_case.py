#Write a proggram to print state full name according to short name.
name = input("Enetr a short name : ")
match name :
    case "MH":
        print("MAHARASTRA")
    case "MP":
        print("MADHAY PRADESH")
    case "RJ":
        print("RAJSTHAN")
    case "UP":
        print("UTTER PRADESH")
    case _:
        print("Not valid Name")