# sort tuples by second value
print(" sort tuples by second value")
data=eval(input("Enter list of tuples: "))
res=sorted(data, key = lambda x: x[1])
print("sorted: ",res)


#tuple list to dictionary
print("tuple list to dictionary")

dat=eval(input("Enter tuples: "))
result=dict(dat)
print("dictionary:",result)
