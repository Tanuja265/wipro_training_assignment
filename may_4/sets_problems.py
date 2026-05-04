#unique elements from two lists
from unittest import result

print("unique elements from two lists")
list1=list(map(int,input("Enter list1: ").split()))
list2=list(map(int,input("Enter list2: ").split()))
result=set(list1).union(set(list2))
print(result)

#check common elements
print("check common elements")
l1=list(map(int,input("Enter list1: ").split()))
l2=list(map(int,input("Enter list2: ").split()))

if set(l1) & set(l2):
    print("yes")
else:
    print("no")