import math
l=500
h=1000

nums=[]
for i in range(2, int(math.sqrt(h))+1):
    nums.append(i)

def primegenerator(nums):
    for l in range(0, int(math.sqrt(max(nums)))):
        pivot = nums.pop(l)
        for i in nums:
            if i % pivot == 0:
                nums.remove(i)
        nums.insert(l, pivot)
    return nums

print(primegenerator(nums))

elements=[]
for i in range(l,h+1):
    elements.append(i)


primes=[]
for i in elements:
    if i==2 or i==3 or i==5 or i==7:
        primes.append(i)
    else:
        for j in nums:
            if i%j==0:
                break
        else:
            primes.append(i)

print(primes)