#wap to print reverse each word in string.
string = "My name is Anup and my city name is Akola"
print(string)
anup = string.split()
for n in anup :
    print(n[::-1],end=" ")