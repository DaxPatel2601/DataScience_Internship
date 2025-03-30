import matplotlib.pyplot as plt
import numpy as np
from Tools.scripts.generate_re_casefix import alpha
import xlrd
import requests

# READ DOCUMENTATION FROM OFFICIAL MATPLOTLIB SITE
# https://matplotlib.org/
#
# And generate following graphs.

# GRAPH 1 :
#
# Create histogram of following data
# price = [180,187,174,160,155,157,140,145,148,155]


# plt.hist(price, bins=5, color="RED", edgecolor='black', density=True, alpha=0.5)
# plt.xlabel("Product")
# plt.ylabel("Price")
# plt.title("Price Analysis")
# plt.show()
#
# GRAPH 2 :
#
# Create a scatter plot of following data
# matches = [1,2,3,4,5]
# rohit = [25,15,45,70,65]


# plt.scatter(matches,rohit,label="Rohit",marker="*",linewidths=2,edgecolors="RED",color="GREEN")
# plt.xticks(matches)
# plt.xlabel("Matches")
# plt.ylabel("Rohit Score")
# plt.title("Matches score analytics")
# plt.legend()
# plt.show()

# GRAPH 3 :

# Create a scatter plot for multiple parameters against values from following data
# matches = [1,2,3,4,5]
# rohit = [25,15,45,70,65]
# kohli = [17,12,55,42,35]
# dhawan =  [10,47,23,17,94]
#
# plt.scatter(matches,rohit,label="ROHIT",marker="o")
# plt.scatter(matches,kohli,label="KOHLI",marker="s")
# plt.scatter(matches,dhawan,label="DHAWAN",marker="d")
# plt.xticks(matches)
# plt.xlabel("Matches")
# plt.ylabel("Score")
# plt.title("Cricket Match Score Analysis")
# plt.legend()
# plt.grid(alpha=0.2)
# plt.show()

# GRAPH 4 :
# Crate a scatter plot graph for year wise car brand’s sales data.
# ( it is used to identify which company had highest selling in particular year )

# years = [2018, 2019, 2020, 2021, 2022]
# toyota_sales = [1200, 1300, 1100, 1400, 1500]
# honda_sales = [950, 1050, 1000, 1100, 1200]
# ford_sales = [800, 900, 850, 950, 1000]
#
#
# plt.scatter(years,toyota_sales,label="TOYOTA")
# plt.scatter(years,honda_sales,label="HONDA")
# plt.scatter(years,ford_sales,label="FORD")
#
# plt.xlabel("Years")
# plt.ylabel("Player Score")
# plt.title("Cricket Match Score Analysis")
# plt.legend()
# plt.xticks(years)
# plt.grid(alpha=0.2)
# plt.show()
#


# GRAPH 5:
#
# Create a horizontal bar graph as shown in below output from given data.

# clothing_items = ['Trousers', 'Shirts', 'Jeans', 'T-Shirts']
# sales = [120, 180, 150, 200]
#
# plt.barh(clothing_items,sales)
# plt.show()


# GRAPH 6 :
#
# XLRD + BAR GRAPH
#
# Allow user to insert name of the player. Generate bar graph of match vs runs of that player.
#
# https://docs.google.com/spreadsheets/d/1dWZm_w9sb88TNmykPuJd3yVxQxhRCzB2YRSCKfJo4iI/edit?usp=sharing

# sheet=xlrd.open_workbook("mydata.xlsx").sheet_by_index(0)
#
# matches=[i for i in range(1,sheet.nrows)]
# score=[]
# user_player=input("Enter Player Name:").upper().strip()
#
# for i in range(1,sheet.ncols):
#     if user_player==sheet.cell_value(0,i):
#         for j in range(1,sheet.nrows):
#             score.append(sheet.cell_value(j,i))
#         plt.plot(matches,score)
#         plt.xlabel("Matches")
#         plt.ylabel("Score")
#         plt.title(f"{user_player} Cricket Score Analysis")
#         plt.grid(alpha=0.5)
#         plt.show()
#         break
#
# else:
#     print("Player is not found")


# GRAPH 8 :
#
#
# CREATE HORIZONTAL BAR GRAPH ( Y AXES STATE NAMES, X AXES TOTAL CASES ) FROM BELOW API ( API/REQUESTS PACKAGE + BAR GRAPH )
#
# https://api.rootnet.in/covid19-in/stats/latest


url=("https://api.rootnet.in/covid19-in/stats/latest")
data=requests.get(url)
mydata=data.json()

state_names=[]
cases=[]



for i in range(0,len(mydata["data"]["regional"])):
    state_names.append(mydata["data"]["regional"][i]["loc"])
    cases.append(mydata["data"]["regional"][i]["deaths"])



plt.barh(state_names,cases)

plt.show()
