import numpy as np

# create two 3*3 matrix with random integers from 1 to 20
# create two 3*3 matrix with random integers from 1 to 20

arr1=np.random.randint(0,20,9).reshape(3,3)
print(arr1)
arr2=np.random.randint(0,20,9).reshape(3,3)
print(arr2)

# perform elements wise addition , substraction , multiplication

arr3=arr1+arr2
# print(arr3)

arr4=arr1-arr2
# print(arr4)

arr5=arr1*arr2
# print(arr5)


# dot product


print(np.dot(arr1,arr2))