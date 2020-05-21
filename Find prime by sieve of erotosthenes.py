

num=[x for x in range(0,1000) if x>1]
max=len(num)+1
s=0


pivot=num.pop(0)
for i  in num:
    if i%pivot==0:
        num.remove(i)
num.insert(0,pivot)
print(num)

pivot=num.pop(1)
print(pivot)
for i  in num:
    if i%pivot==0:
        num.remove(i)
num.insert(1,pivot)

pivot=num.pop(2)
print(pivot)
for i  in num:
    if i%pivot==0:
        num.remove(i)
num.insert(2,pivot)

pivot=num.pop(3)
print(pivot)
for i  in num:
    if i%pivot==0:
        num.remove(i)
num.insert(3,pivot)

pivot=num.pop(4)
print(pivot)
for i  in num:
    if i%pivot==0:
        num.remove(i)
num.insert(4,pivot)

pivot=num.pop(5)
print(pivot)
for i  in num:
    if i%pivot==0:
        num.remove(i)
num.insert(5,pivot)

pivot=num.pop(6)
print(pivot)
for i  in num:
    if i%pivot==0:
        num.remove(i)
num.insert(6,pivot)

pivot=num.pop(7)
print(pivot)
for i  in num:
    if i%pivot==0:
        num.remove(i)
num.insert(7,pivot)

pivot=num.pop(8)
print(pivot)
for i  in num:
    if i%pivot==0:
        num.remove(i)
num.insert(9,pivot)

pivot=num.pop(10)
print(pivot)
for i  in num:
    if i%pivot==0:
        num.remove(i)
num.insert(10,pivot)

print(num)

for i in num:
    for  j in range(2,i):
        if i%j==0:
            print("found not prim:",i)
