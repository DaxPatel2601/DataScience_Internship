import numpy as np

arr3=np.random.randint(100000,200000,500).reshape(5,5,20)

print(arr3)
user=int(input("Enter Value:"))
value_found=False

for i in arr3:
    for j in i:
        for k in j:
            if user==k:
                print("Value Found")
                value_found=True
                break

if value_found==False:
    print("Value not Found")


