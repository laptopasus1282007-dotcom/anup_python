#check a whether charcter is a vovel, consonent,or not an alphabet.
char = input('Enter a charcter : ')

if char >= 'a' and char <= 'z' or char >='A' and char <= 'Z' :
    if char in ("a,e,i,o,u,A,E,I,O,U") :
        print("charcter is a vovel")

    else :
     print("charcter is a consonent")

else : 
    print("Charcter is not a Alphabet")