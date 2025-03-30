import numpy as np

# create an array 20 random integer between 1 to 100

arr=np.random.randint(0,100,20)
arr1=np.array([])
print(arr)
arr2=np.array([])

for i in range(0,len(arr)):
    if arr[i]>50:
        arr2=np.append(arr1,arr[i])
print(arr2)