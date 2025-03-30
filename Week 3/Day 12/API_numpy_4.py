# Create a NumPy array of daily temperatures for one year (365 days)
import numpy as np

arr=np.random.randint(-20,50,365)

# Find the hottest day
print(arr.max())
print(np.where(arr==arr.max()))

# find the coldest day
print(arr.min())
print(np.where(arr==arr.min()))

# number of days above 30°C.

print(len(arr[np.where(arr>30)]))


