
import datetime
start=datetime.datetime.now()
nums=[2,11,5,13,6,13,7,19,23,29]
nums.sort()
key=0
def binary(nums,key):

    low=0
    high=len(nums)-1

    while(low<=high):
        mid=int((low+high)/2)
        if (nums[mid]==key):
            return ("found at index",mid)
        elif(nums[mid]>key):
            high=mid-1
        elif(nums[mid]<key):
            low=mid+1
        else:
            pass
    else:
        return ("Not found",None)
comment,index=binary(nums,key)
print(comment,index)

print(datetime.datetime.now()-start)





