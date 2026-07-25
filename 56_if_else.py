# Check whether a character is uppercase or lowercase and convert it.
char = input("Enter a single character: ")

if len(char) != 1 or not char.isalpha():
    print("Please enter exactly one letter.")
else:
    if char.isupper():
        print("Converted to lowercase:", char.lower())
    else:
        print("Converted to uppercase:", char.upper())
