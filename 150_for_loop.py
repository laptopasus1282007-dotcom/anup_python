# Count digits in a given number.

number_str = input("Enter a number: ").strip()

# Keep the sign separate so it does not count as a digit.
if number_str.startswith(('-', '+')):
    number_str = number_str[1:]

count = 0
for ch in number_str:
    if ch.isdigit():
        count += 1

print(f"The number contains {count} digit{'s' if count != 1 else ''}.")
