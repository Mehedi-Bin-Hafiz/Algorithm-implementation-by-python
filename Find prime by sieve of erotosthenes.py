nums=[x for x in range(2,101)]
print(nums)

print("\n\n")
for l in range(0,12):
    pivot = nums.pop(l)
    for i in nums:
        if i % pivot == 0:
            nums.remove(i)
    nums.insert(l,pivot)

print(nums)
print("The number of prime numbers: ",len(nums))
