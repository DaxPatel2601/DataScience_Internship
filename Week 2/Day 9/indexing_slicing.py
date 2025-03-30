import numpy as np

# create an array of 8*8 with value from 1 to 64

arr=np.random.randint(0,64,64).reshape(8,8)
print(arr)

# extract third row and fifth column sepratily

rows,cols=arr.shape

for i in range(0,rows):
    if i+1==3:
        print("Third row is :",arr[i])
        break

#for transpose the matrix
arr3=np.transpose(arr)

for i in range(0,rows):
    if i+1==4:
        print("Third column is :",arr3[i])
        break


# extract corner element
# advanced indexing
# np.ix_

# a = np.ix_([0,-1],[0,-1])
# b = arr[a]
# print(b)


# Reverse the order of element along the rows

for i in arr:
    arr1=i[::-1]
    print(arr1)

