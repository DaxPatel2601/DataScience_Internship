import numpy as np

# create 5*5 Numpy array with integer between 10 and 50

arr=np.random.randint(10,50,25).reshape(5,5)
print(arr)
print("\n")


# replace all even numbers with -1
rows,cols = arr.shape

# for i in range(0,rows):
#     for j in range(0,cols):
#         if arr[i][j]%2==0:
#             arr[i][j]=-1
# print(arr)

# reshape the array into a 1D array and than back into 5*5 array

arr2=arr.reshape(25)
print(arr2)

