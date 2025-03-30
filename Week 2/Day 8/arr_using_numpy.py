import numpy as np

# creating 1D array using numpy
arr1=np.array([10,2,3,4])
# print(arr1)

# creating 2D array using numpy
arr2=np.array([[10,2,3,4],[50,6,7,8]])
# print(arr2)

# creating 3D array using numpy
arr3=np.array([[[10,2,3,4],[50,6,7,8]],[[40,5,8,6],[41,5,7,8]]])
# print(arr3)

# checking type of array3
# print(type(arr3))

# print dimentionals of array
# print(arr3.ndim)

# sorting arr1
# arr1.sort(axis=0)
# print(arr1)

# sorting arr2
# arr2.sort()
# print(arr2)

# arr2.sort(axis=1)
# print(arr2)

# arr2.sort(axis=0)
# print(arr2)

# accesing elemnts of arr1
# print(arr1[2])

# accessing elements of arr2
# print(arr2[0][1])

# accessing elements of arr3
# print(arr3[0][1][2])

# printing all elements of arr1 using for loop
# for i in arr1:
#     print(i)

# printing all elements of arr2 using for loop
# for i in arr2:
#     for j in i:
#         print(j)

# printing all elements of arr3 using for loop
# for i in arr3:
#     for j in i:
#         for z in j:
#             print(z)


# printing all elements of arr1 using nditer method
# for i in np.nditer(arr1):
#     print(i)

# printing all elements of arr2 using nditer method
# for i in np.nditer(arr2):
#     print(i)

# printing all elements of arr3 using nditer method
# for i in np.nditer(arr3):
#     print(i)

# sum of all element in arr1
# print(arr1.sum())

# sum of all element in arr2
# print(arr2.sum())

# sum of all element in arr3
# print(arr3.sum())


# filtering
# print(arr1[arr1>5])
