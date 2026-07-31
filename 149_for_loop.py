# Write a program to print Fibonacci series
# (0 1 1 2 3 5 8 13 21 34 55).

count = 10
first, second = 0, 1
sequence = []

for _ in range(count):
    sequence.append(str(first))
    first, second = second, first + second

print("Fibonacci series:", " ".join(sequence))
