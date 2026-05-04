# Find Second Largest Number
print("Find Second Largest Number")

nums=list(map(int,input("Enter numbers: ").split()))
nums.sort()

print("second largest number is ",nums[-2])

#Rotated List by K steps

print("Rotated List by K steps")

que=list(map(int,input("Enter numbers: ").split()))
k=int(input("Enter number of steps: "))
k=k%len(que)
res=que[-k:] + que[:-k]
print(res)


#missing numbers

print("missing numbers")

queu=list(map(int,input("Enter numbers: ").split()))

n=len(queu) + 1
total=n*(n+1)//2
print(total-sum(queu))

#moves zero to end

print("moves zero to end")

numb=list(map(int,input("Enter numbers: ").split()))
nz=[x for x in numb if x!=0]
zer=[0]*numb.count(0)
print(nz+zer)


#pairs with given sum

print("pairs with given sum")

numbe=list(map(int,input("Enter numbers: ").split()))
tar=int(input("Enter target number: "))
seen=set()
for num in numbe:
    if tar-num in seen:
        print("pair:",num,tar-num)
    seen.add(num)



