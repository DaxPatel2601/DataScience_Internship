import numpy as np


arr=np.array([
[101, 250.50, 10, 1],
[102, 120.00, 5, 2],
[103, 310.75, 15, 3],
[104, 90.25, 0, 1],
[105, 500.00, 20, 4],
[106, 75.50, 0, 2],
[107, 150.00, 10, 3],
[108, 600.00, 25, 4],
[109, 220.00, 5, 1],
[110, 130.00, 8, 2]
])

#Filtering Transactions
#a. Find all transactions where the purchase amount is greater than $200.

print(arr[np.where(arr>200)])

#b. Extract all transactions where a discount of more than 10% was applied.
discount=np.array([])
for i in range(0,len(arr)):
    discount=np.append(discount,arr[i][2])
print(discount)


#7. Category-Based Analysis
#a. Extract all transactions that belong to Category Code 3.

for i in range(0,len(arr)):
        if arr[i][3]==3:
            print(arr[i])

#b. Find the total purchase amount for each category.

rows,cols=np.shape(arr)

sum_all_1=0
sum_all_2=0
sum_all_3=0
sum_all_4=0
sum_all_5=0
for i in range(0,rows):
    for j in range(0,cols):
        if arr[i][j] == 1:
            sum_all_1 += arr[i][1]

        if arr[i][j] == 2:
            sum_all_2 += arr[i][1]

        if arr[i][j] == 3:
            sum_all_3 += arr[i][1]

        if arr[i][j] == 4:
            sum_all_4 += arr[i][1]

        if arr[i][j] == 5:
            sum_all_5 += arr[i][1]

print("Category 1",sum_all_1)
print("Category 2:",sum_all_2)
print("Category 3:",sum_all_3)
print("Category 4:",sum_all_4)
print("Category 5:",sum_all_5)


