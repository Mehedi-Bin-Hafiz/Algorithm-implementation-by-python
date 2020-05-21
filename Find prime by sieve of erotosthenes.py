

num=[x for x in range(0,100) if x>1]
for l in range(0,11):
    pivot=num.pop(l)
    for i  in num:
        if i%pivot==0:
            num.remove(i)
    num.insert(l,pivot)
print(num)
print(len(num))






