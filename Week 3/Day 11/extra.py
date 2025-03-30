import numpy as np

arr=np.array([[1,2,3],[4,5,6]])

sum_all=np.sum(np.nditer(arr))
print(sum_all/len(arr))
print(arr)


