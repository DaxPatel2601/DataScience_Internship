import xlrd
import matplotlib.pyplot as plt
import numpy as np

#1. Load hotel reviews dataset and Print first hotel’s name.

sheet=xlrd.open_workbook("hotel_revies.xlsx").sheet_by_index(0)
print(sheet.cell_value(1,11))


# Print total number of rows.
print(sheet.nrows)
# Print total number of Columns.
print(sheet.ncols)
# Allow user to insert hotel Name, Print hotel found or Not found

# user_input=input("Enter Hotel Name:")
#
# for i in range(1,sheet.nrows):
#     if user_input==sheet.cell_value(i,11):
#         print("found")
#         break
# else:
#     print("Not Found")


# Allow user to insert hotel name, print hotel's details. For example Categories, city, state province ‘ address etc.

# user_input=input("Enter Hotel Name:")
#
# for i in range(1,sheet.nrows):
#     if user_input==sheet.cell_value(i,11):
#         print(f"Category is : {sheet.cell_value(i,4)}")
#         print(f"City is : {sheet.cell_value(i,6)}")
#         print(f"State Province : {sheet.cell_value(i,5)}")
#         print(f"Address if : {sheet.cell_value(i,3)}")
#         exit()
# else:
#     print("Not Found")


# Allow user to insert hotel name print total rating average of that hotel.

# user_input=input("Enter Hotel Name:")
# total_rating=[]
# is_found=False
#
# for i in range(1,sheet.nrows):
#     if user_input==sheet.cell_value(i,11):
#         total_rating.append(sheet.cell_value(i,17))
#         is_found=True
#
# if is_found==False:
#     print("Not Found")
# else:
#     print(f"{np.mean(total_rating)} is Average Rating")

# Allow user to insert hotel name print pie chart and bar graph of that hotel's Star wise rating count.
# For Example 1 star - 12, 2 star - 8, 3 star - 23, 4 star - 35, 5 star - 120

# user_input=input("Enter Hotel Name:")
# total_rating=[]
# rating=[]
# is_found=False
#
# for i in range(1,sheet.nrows):
#     if user_input==sheet.cell_value(i,11):
#         total_rating.append(sheet.cell_value(i,17))
#         is_found=True
#
# if is_found==False:
#     print("Not Found")
# else:
#     for i in range(1,6):
#         rating.append(total_rating.count(i))
#
#     fig , ax = plt.subplots(1,2,figsize=(10,8))
#     ax[0].pie(rating,labels=["1","2","3","4","5"],autopct="%.2f%%")
#     ax[0].set_title(user_input)
#
#
#     ax[1].bar(["1","2","3","4","5"],rating)
#     ax[1].set_title(user_input)
#     ax[1].set_xlabel("Rating")
#     ax[1].set_ylabel("Count Of Rating")
#     plt.tight_layout()
#     plt.show()


# Allow user to insert hotel names until User inserts stop. Print bar graph of Average rating of those entered hotel's.



# total_rating=[]
# rating=[]
# star=["1","2","3","4","5"]
# is_found=False
# user_enter_hotel_name=[]
# average=[]
#
# while True:
#     user_input = input("Enter Hotel Name:")
#     if user_input!="stop":
#
#         for i in range(1,sheet.nrows):
#             if user_input==sheet.cell_value(i,11):
#                 total_rating.append(sheet.cell_value(i,17))
#                 is_found=True
#
#         if is_found==False:
#             print("Not Found")
#         else:
#             average.append(float(np.mean(total_rating)))
#             user_enter_hotel_name.append(user_input)
#             print(user_enter_hotel_name)
#             print(average)
#
#     else:
#         plt.bar(user_enter_hotel_name, average)
#         plt.show()
#         exit()


# Allow user to insert any 3 hotel names.
# Print pie chart of all 3 hotel's rating wise count ( same as question  7 ) in single frame.
# ( 3 pie chart of 3 hotels for comparison  ).

count=1
user_input_name=[]
total_rating_1=[]
total_rating_2=[]
total_rating_3=[]
rating_1=[]
rating_2=[]
rating_3=[]
star=["1","2","3","4","5"]
is_found=False

while count < 4 :
    user_input=input("Enter Hotel Name:")

    for i in range(1,sheet.nrows):
        if user_input==sheet.cell_value(i,11):

            if count==1:
                total_rating_1.append(sheet.cell_value(i,17))
                count += 1
            elif count==2:
                total_rating_2.append(sheet.cell_value(i, 17))
                count += 1
            elif count==3:
                total_rating_3.append(sheet.cell_value(i, 17))
            is_found = True
    count += 1



    if is_found==False:
        print("Not Found")
    else:
        for i in range(1,6):
            rating_1.append(total_rating_1.count(i))
            rating_2.append(total_rating_2.count(i))
            rating_3.append((total_rating_3.count(i)))


print(rating_1)
print(rating_2)
print(rating_3)

fig , ax = plt.subplots(1,3,figsize=(10,8))

ax[1].bar(star,rating_1)
ax[1].set_title(user_input_name[0])
ax[1].set_xlabel("Rating")
ax[1].set_ylabel("Count Of Rating")


ax[1].bar(star,rating_2)
ax[1].set_title(user_input_name[1])
ax[1].set_xlabel("Rating")
ax[1].set_ylabel("Count Of Rating")

ax[2].bar(star,rating_3)
ax[2].set_title(user_input_name[2])
ax[2].set_xlabel("Rating")
ax[2].set_ylabel("Count Of Rating")

plt.tight_layout()
plt.show()
