numbers=(10,20,30,40,50)
print(numbers)

print(numbers[0])
print(numbers[1])
print(numbers[2])

print(numbers[-1])

print(numbers[1:4])

#you cant modify tuples ---they are immutable
#numbers[1]=99

for num in reversed(numbers):
    print(num)


#mixed data types

data=("tanu", 25, 5500, True)
print(data)

#tuple packing
person=("tanu", 25, "engineer")
print(person)

#tuple unpacking

name, age, profession = person

print(name)
print(age)
print(profession)