import xlrd

sheet=xlrd.open_workbook("cricket.xlsx")
sheet=sheet.sheet_by_index(0)


# Print total number of rows.
print("Total rows are : ",sheet.nrows)

# Print total number of columns.
print("Total columns are : ",sheet.ncols)

# Print total number of matches
print("Total Numbers Of Matches are : ", sheet.ncols-1)

# print Total numbers of players
print("Total Number of players are : ", sheet.nrows-1)

# Print name of all players
for i in range(1,sheet.nrows):
    print(sheet.cell_value(i,0))

# Print score of all matches of VIRAT

for i in range(1,sheet.ncols):
        print(sheet.cell_value(2,i))

# Allow user to insert player name, print found or not found

user_entered_player=input("Enter Player Name :").upper()
# for i in range(1,sheet.nrows):
#     if user_entered_player==sheet.cell_value(i,0):
#         print("Player Found")
#         break
# else:
#     print("Player Not found")

# Allow user to insert player name, print latest score of that player

# for i in range(1,sheet.nrows):
#     if user_entered_player==sheet.cell_value(i,0):
#         print(sheet.cell_value(i,sheet.ncols-1))
#         break
# else:
#     print("Player is not found")

# Allow user to insert name of player, print score of all matches of that player.

# for i in range(1,sheet.nrows):
#     if user_entered_player==sheet.cell_value(i,0):
#         for j in range(1,sheet.ncols):
#             print(sheet.cell_value(i,j))
#         break
# else:
#     print("Player is not found")

# Allow user to insert player name, store all matches data fo that player in a list.
score=[]

# for i in range(1,sheet.nrows):
#     if user_entered_player==sheet.cell_value(i,0):
#         for j in range(1,sheet.ncols):
#             score.append(sheet.cell_value(i,j))
#         break
# else:
#     print("Player is not found")
# print(score)

# Allow user to insert player name, print High score, Low Score, Average score of that player.

max_score=0
total_score=0
min_score=0

for i in range(1,sheet.nrows):
    if user_entered_player==sheet.cell_value(i,0):
        min_score=sheet.cell_value(i,1)
        for j in range(1,sheet.ncols):
            total_score+=sheet.cell_value(i,j)
            if max_score<sheet.cell_value(i,j):
                max_score=sheet.cell_value(i,j)
            if min_score>sheet.cell_value(i,j):
                min_score=sheet.cell_value(i,j)
        break
else:
    print("Player is not found")



print("Maximum Score is ",max_score)
if min_score!=0:
    print("Minimum Score is ",min_score)
print("Total Score is ",total_score)
print("Average Score is ",total_score/(sheet.ncols-1))




















