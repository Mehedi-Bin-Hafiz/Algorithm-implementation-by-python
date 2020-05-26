import datetime
begin_time = datetime.datetime.now()
nums=[2,11,5,13,6,13,7,19,23,29]
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

print(datetime.datetime.now() - begin_time)