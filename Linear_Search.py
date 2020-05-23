
nums=[2,3,5,7,11,13,13,19,23,29]


def linear(nums,key):
    global ind
    for i in nums:
        if i==key:
            ind=nums.index(i)
            return ("Found")
    else:
        ind=None
        return ("Not found")

key=int(input("Enter your key: "))

res=linear(nums,key)

print(key,"is ", res , " at ", ind)