numbers=list(map(int,input("enter a number").split()))
for num in numbers:
    if num%2==0:
        print(num)

print(list(filter(lambda x: x%2==0,numbers)))

print("using for")
for i in range(20):
    if i%2==0:
        print(i)


