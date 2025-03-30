import numpy as np

# Generate random monthly airline passenger numbers for 5 years.
arr=np.random.randint(0,500,60).reshape(5,12)
print(arr)

#Find the month with the highest and lowest passengers
max_passengers=np.where(arr==arr.max())
print(arr[max_passengers])

min_passengers=np.where(arr==arr.min())
print(arr[min_passengers])

# Calculate yearly average passengers and growth rate.

for i in range(0,len(arr)):
    print((np.sum(arr[i]))/len(arr[i]))

