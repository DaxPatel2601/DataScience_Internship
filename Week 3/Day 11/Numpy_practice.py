import numpy as np

arr=np.random.randint(1000,10000,1000).reshape(10,10,10)
print(arr)
is_found=False
# user_value=int(input("Enter Number:"))

# for i in arr:
#     for j in i:
#         for k in j:
#             if k==user_value:
#                 print(f"{user_value} is Found")
#                 is_found=True
#                 break
#
# if is_found==False:
#     print(f"{user_value} is not Found")

# second method for searching elements

# for i in arr:
#     for j in i:
#         for k in j:
#             if k==user_value:
#                 print(f"{user_value} is Found")
#                 is_found=True
#                 exit()
# else:
#     print(f"{user_value} is not Found")

# Third way

# for i in np.nditer(arr):
#     if user_value==i:
#         print("Value Found")
#         break
# else:
#     print("Value is Not Found")

# where method
# where method is retrun index position

index = np.where((arr>=1000)&(arr<=2000))
print(arr[index])

# with the use of argmax and argmin , its retrun index position of maximum and minimum value of any array

# maximum=np.argmax(arr)
# minimum=np.argmin(arr)
# print(maximum)
# print(minimum)
# print(arr[maximum])
#

maximum=np.max(arr)
print(maximum)

index = np.where(arr==maximum)
print(index)

