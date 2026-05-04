numbers=[10,20,30,40,50]

print(numbers)

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

# negative idexing
print(numbers[-1])
print(numbers[-2])


#modifying list elements
numbers[1]=99
print(numbers)

#adding elements to list
numbers.append(60)
print(numbers)

numbers.insert(1,99)
print(numbers)

numbers.remove(99)  #remove particular number
print(numbers)

numbers.pop()
print(numbers) #remove last number

print(len(numbers))

for num in numbers:
    print(num)

#slice
numbers=[10,20,30,40,50]
print(numbers[1:4])