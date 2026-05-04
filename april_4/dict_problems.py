#count frequency
print("count frequency")
nums=list(map(int,input("Enter numbers: ").split()))
freq={}
for num in nums:
    freq[num]=freq.get(num,0)+1
print("frequency:", freq)

#key with maximum value
print("key with maximum value")

data=eval(input("Enter dictionary:"))
res=max(data, key=data.get)
print("max key:", res)

#merge dictionaries
d1=eval(input("Enter first dictionary: "))
d2=eval(input("Enter second dictionary: "))
d1.update(d2)

print("merged:", d1)


#invert dictionary
print("invert dictionary")
dat=eval(input("Enter dictionary: "))
result= {v:k for k,v in dat.items()}

print(result)





