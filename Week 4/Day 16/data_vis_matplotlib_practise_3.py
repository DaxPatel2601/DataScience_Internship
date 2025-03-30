import matplotlib.pyplot as plt
import xlrd
import numpy as np

#
# PRACTICE WORK GRAPH 4 :
#
# CREATE PIE CHART OF PLAYER WISE CONTRIBUTION IN ENTIRE SERIES FROM BELOW EXCEL DATA ( XLRD + PIE CHART )
#
# LINK : https://docs.google.com/spreadsheets/d/1dWZm_w9sb88TNmykPuJd3yVxQxhRCzB2YRSCKfJo4iI/edit?usp=sharing

sheet=xlrd.open_workbook("mydata.xlsx").sheet_by_index(0)

player_name=[]
player_score=[]
matches=[]
barwidth=0.15

for i in range(1,sheet.ncols):
    total_score=0
    for j in range(1,sheet.nrows):
        total_score+=sheet.cell_value(j,i)
    player_score.append(total_score)
    player_name.append(sheet.cell_value(0,i))
    matches.append(sheet.cell_value(i,0))


plt.pie(player_score,labels=player_name,autopct="%.2f%%")
plt.show()




