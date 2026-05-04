#SETS --does not allow duplicates

numbers={10,20,30,40}

print(numbers)

numbers={10,20,20,30,30,40}

print(numbers)

#Add
numbers.add(50)
print(numbers)

numbers.remove(50)
print(numbers)

for num in numbers:
    print(num)

print(len(numbers))


set1={1,2,3}
set2={3,4,5}

#UNION
result=set1.union(set2)
print(result)

#INTERSECTION

result=set1.intersection(set2)
print(result)

#difference

result=set1.difference(set2)
print(result)

#LIST TO SET (remove duplicates)

numbers=[1,2,2,2,3,4,4,4,5]
unique=set(numbers)
print(unique)