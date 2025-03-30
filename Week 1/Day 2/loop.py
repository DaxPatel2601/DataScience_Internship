# print all items of list using for loop

cities=["Ahemdabad","Surat","Rajkot","Amreli"]
user_city=str(input("Enter your city which you may searching:"))

for i in cities:
    if user_city==i:
        print("City is found")
        break
else:
   print("City is not found")
