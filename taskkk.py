
arr=[]
arr2=[]
arr3=[]
for i in range(2):
    for j in range(1):
        for k in range(1):
            arr.append(i * j)
        arr2.append(arr)
    arr3.append(arr2)

print(arr3)