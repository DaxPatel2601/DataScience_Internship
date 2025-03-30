import requests
import numpy as np

data=requests.get("https://api.rootnet.in/covid19-in/stats/latest")
my_data=data.json()

# to change data type of array is with use of dtype+np.interger

arr=np.array([],dtype=np.int64)

for i in range(0,len(my_data["data"]["regional"])):
    arr=np.append(arr,my_data["data"]["regional"][i]["totalConfirmed"])

print(arr)

sum_all=np.sum(arr)
print("Sum of All Elements is : ",sum_all)

print(arr[np.where(arr>100000)])

# user_input=int(input("Enter Value:"))
#
# index=np.where(user_input==arr)
# print(index)
#
# arr2=np.sort(arr)
# arr3=arr2[::-1]
# arr4=np.array([])
# for i in range(0,10):
#     arr4=np.append(arr4,arr3[i])
#
# print(arr4)


# replace all values which is greater than 100000 with -1
print(arr)
arr[arr<100000]=-1
print(arr)

# print maximum and minimum cases
maximim=np.argmax(arr)
minimum=np.argmin(arr)

print(arr[maximim])
print(arr[minimum])




