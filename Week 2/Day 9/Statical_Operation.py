import numpy as np

# genrate 7*7 arr
arr=np.random.randint(0,100,49).reshape(7,7)
print(arr)

# find mean, median of the entire array

print("Mean : ",arr.mean())
print("Meadian :",int(arr.mean()))

# find column wise mean and row wise mean sum

rows,cols=arr.shape

for i in range(0,rows):
    print(f"{i+1} Row Mean is : ",arr[i].mean())

print("\n")

for j in range(0,cols):
    print(f"{j+1} Column Mean is :",arr[j].mean())


