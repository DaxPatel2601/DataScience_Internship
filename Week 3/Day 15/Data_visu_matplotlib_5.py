#Xlrd + Matplotlib

# Excel Link : https://docs.google.com/spreadsheets/d/1dWZm_w9sb88TNmykPuJd3yVxQxhRCzB2YRSCKfJo4iI/edit?usp=sharing
# Create a bar graph of player names vs total score of that player in all matches.


import matplotlib.pyplot as plt
import xlrd

sheet=xlrd.open_workbook("mydata.xlsx")
sheet=sheet.sheet_by_index(0)

players=[]
total_score=[]

for i in range(1,sheet.ncols):
    players.append(sheet.cell_value(0,i))
for i in range(1,sheet.ncols):
    total_score_each=0
    for j in range(1,sheet.nrows):
        total_score_each+=sheet.cell_value(j,i)
    total_score.append(total_score_each)

plt.bar(players,total_score)
plt.xlabel("Player Name")
plt.ylabel("Total Runs")
plt.title("Player's Total Score Analysis")
plt.show()


