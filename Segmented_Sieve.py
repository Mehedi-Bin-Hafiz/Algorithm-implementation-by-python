import math
a=2
b=1000


print(int(math.sqrt(b)))
element=[]
for i in range(2,int(math.sqrt(b))+1):
    element.append(i)

print(element)
def primegenerator(nums):
    maxi=int(math.sqrt(max(nums)))
    for l in range(0, maxi+1):
        pivot = nums.pop(l)
        for i in nums:
            if i % pivot == 0:
                nums.remove(i)
        nums.insert(l, pivot)
    return nums

newlis=primegenerator(element)
print(newlis)
yourrange=[]
for i in range(a,b+1):
    yourrange.append(i)

print(yourrange)

primenumber=[]
for i in yourrange:
    if i == 2 or i==3 or i==5 or i==7 or i==9 or i ==11:
       primenumber.append(i)
    else:
        for j in newlis:
            if i%j == 0:
                break
        else:
            primenumber.append(i)

print(primenumber)
