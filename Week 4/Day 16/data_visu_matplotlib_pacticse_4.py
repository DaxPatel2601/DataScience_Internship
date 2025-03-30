from cProfile import label

import matplotlib.pyplot as plt
import numpy as np
import xlrd

# CREATE A MULTIPLE BAR GRAPH OF ALL PLAYERS IN MATCH VS SCORE PATTERN. ( MULTIPLE BAR GRAPH + XLRD )
# LINK : https://docs.google.com/spreadsheets/d/1dWZm_w9sb88TNmykPuJd3yVxQxhRCzB2YRSCKfJo4iI/edit?usp=sharing


sheet=xlrd.open_workbook("mydata.xlsx").sheet_by_index(0)
players={}
total_matches=[]
player_names=[]
barwidth=0.05

for i in range(1,sheet.ncols):
    score_each=[]
    for j in range(1,sheet.nrows):
        score_each.append(sheet.cell_value(j,i))
    players[sheet.cell_value(0,i)]=score_each
    player_names.append(sheet.cell_value(0,i))
    total_matches.append(sheet.cell_value(i,0))

print(players)
print(total_matches)


for i in range(0,len(total_matches)):
    plt.bar(np.arange(len(total_matches)),int(players.values())[i],width=barwidth)

plt.show()



















