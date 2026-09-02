#Write a program to find the average of array elements. 
list=[]
length=int(input("Enter a length of array elemennts : "))
for number in range(length):
    num=int(input("Enter a Array elements : "))
    list.append(num)
print("list is : ",list)

sum=0
for n in list:
    sum=sum+n
print("Sum of array elements is : ",sum)
print("Average of array elements is : ",sum/len(list))

