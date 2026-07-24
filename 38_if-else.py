#Write a program to check given char is vowel or consonant. 
alphabet = input("Enter a alphabet : ")
#if alphabet == "a" or alphabet == "e" or alphabet == "i" or alphabet == "o" or alphabet == "u" :
if alphabet in "aeiouAEIOU" :
    print("Alphabet is vovel")
else:
    print("Alphabet is Consonant")
