import numpy as np

#  Create a 100x5 NumPy array representing 100 customers and their S most recent purches

arr=np.random.uniform(100,1000000,500).reshape(100,5)

# print(arr)

# The purchase amounts should be random floats between ₹100 and ¥50,000.

index=np.where((arr>100)&(arr<50000))
print(arr[index])

# Find and print the highest and lowest purchase amounts

maximum=arr.max()
print(maximum)

minimum=arr.min()
print(minimum)

# Compute the average purchase amount per customer and store it in a new aray.

# sum=0
# for x in np.nditer(arr):
#     sum+=x
# print("Sum is ",sum)
#
# average=sum/len(arr)
# print("Average is ",average)

arr1=np.array([])
sum_all=0
average_all=0

for i in arr:
    for j in i:
        sum_all+=j
    average_all=sum_all/5
    arr1=np.append(arr1,average_all)    

print(arr1)

# Dctarmine the customer who spent the most overall and print their index

index_hight=np.where(arr==maximum)
print(index)



