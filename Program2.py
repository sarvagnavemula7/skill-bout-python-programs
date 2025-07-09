#Write a Python program to take 5 numbers as input from the user, store them in a list, and then:Print the list in reverse order.
#Print the sum and average of the numbers.

lst=list(map(int,input("Enter list elements:").split()))

print(lst[::-1])
sum=sum(lst)
avg=sum/len(lst)


lst2=[]
for i in range(len(lst)-1,-1,-1):
    lst2.append(lst[i])
print(lst2)
print("sum of elements:",sum)
print("Avg of elements:",avg)
