import datetime

begin_time = datetime.datetime.now()
l=[1,6,3,1,5,8,4,2,1]
l.sort()

key=8
low=0
high=len(l)-1
while(low<=high):
    mid=int((low+high)/2)
    if (l[mid] == key):
        print('found at index',mid)
        break
    elif(l[mid]>key):
        high=mid-1
    elif(l[mid]<key):
        low=mid+1
    else:
        pass
else:
    print("not found")

print(datetime.datetime.now() - begin_time)






