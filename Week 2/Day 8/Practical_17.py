import xlrd

loc=("excel1.xlsx")
sheet=xlrd.open_workbook(loc)
sheet=sheet.sheet_by_index(0)

#allow user to insert player name , stored all scores in temp data structure

# list
# lst_score=[]
# user_player=input("Enter Player Name:").lower()

# for i in range(1,sheet.ncols):
#     if user_player==sheet.cell_value(0,i):
#         for j in range(1,sheet.nrows):
#             lst_score.append(int(sheet.cell_value(j,i)))
#         break
# else:
#     print("Player Not Found")
#
# print(lst_score)

# allow user to insert player name , print lowest score of that player

# for i in range(1,sheet.ncols):
#     if user_player == sheet.cell_value(0,i):
#         lowest_score=sheet.cell_value(1,i)
#         for j in range(1,sheet.nrows):
#             if lowest_score > sheet.cell_value(j,i):
#                 lowest_score=sheet.cell_value(j,i)
#         break
# else:
#     print("Player Not Found")
#
# print("Lowest Score is :",int(lowest_score))

# allow user to insert player names and stores in a variable , print latest score of inserted players

player_name=[]

while True :
    user_player=input(f"Enter Player Name:").lower()
    if user_player!="stop":
        for i in range(1,sheet.ncols):
            if user_player==sheet.cell_value(0,i):
                player_name.append(user_player)
                break
        else:
            print("player not found")
    else:
        break

for i in player_name:
    for j in range(0,sheet.ncols):
        if i==sheet.cell_value(0,j):
            print(sheet.cell_value(0,j),":",int(sheet.cell_value(sheet.nrows-1,j)))
            break











