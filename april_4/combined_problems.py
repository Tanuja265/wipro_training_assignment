#group by frequency
print("group by frequency")

nums=list(map(int,input("enter numbers").split()))
freq={}
for num in nums:
    freq.setdefault(num,[]).append(num)
print("grouped:", freq)

#first non repeating element

print("first non repeating element")
data=list(map(int,input("enter numbers").split()))
freq={}
for num in data:
    freq[num]=freq.get(num,0)+1

for num in data:
    if freq[num]==1:
        print("first non repeating:", num)
        break

#flatten nested list
print("flatten nested list")

nested=eval(input("enter nested list"))
result=[item for sublist in nested for item in sublist]
print(result)
