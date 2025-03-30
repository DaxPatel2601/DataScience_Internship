# GRAPH 3 : XLRD+MATPLOTLIB
#
# Result 1 : https://docs.google.com/spreadsheets/d/1g52xkDE5d_4ypHl0LKam1AkLK0AbeaRdJf6BnXR22Uk/edit?usp=sharing
#
# Result 2 :
# https://docs.google.com/spreadsheets/d/1yB9TlSHY3jOtxvX54ep6dDUE8ADtaiW1pfD8ezjrd8I/edit?usp=sharing
#
# > Can we load two xlsx file in a single python program ?
# > If yes print RAMESH and KATHAN
# > Print horizontal bar graph of all 10 students. Y axes student name, X axes total.

import xlrd
import matplotlib.pyplot as plt
from Tools.scripts.generate_re_casefix import alpha

sheet1=xlrd.open_workbook("RESULT1.xlsx").sheet_by_index(0)
sheet2=xlrd.open_workbook("RESULT2.xlsx").sheet_by_index(0)

print(sheet1.cell_value(1,2))
print(sheet2.cell_value(3,2))

student_name=[]
student_total=[]

for i in range(1,sheet1.nrows):
    student_name.append(sheet1.cell_value(i,2))
    student_total.append(sheet1.cell_value(i,3))

for i in range(1,sheet2.ncols):
    student_name.append(sheet2.cell_value(i,2))
    student_total.append(sheet2.cell_value(i,3))

plt.barh(student_name,student_total)
plt.xlabel("Student Total Score")
plt.ylabel("Student Name")
plt.title("Student Score Analysis")
plt.grid(alpha=0.2)
plt.show()