"""list = [5, 10, 15, 20, 25]
sum = 0
for i in list:
    sum = sum + i

print("Sum:", sum)
print("Average:", sum / len(list))
"""

'''numbers = [4, 6, 8, 7, 3, 5, 1, 12, 10, 13]

count_even = 0
count_odd = 0

for num in numbers:
    if num % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print("Even numbers:", count_even)
print("Odd numbers:", count_odd)
'''

list=[25,30,12,3,21,10]
search_element=12
for i in range (1,6,1):
    if list[i]==search_element:
        print(i)